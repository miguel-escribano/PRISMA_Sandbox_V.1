"""
PRISMA MVP - Scenario Runner
Reads timeline CSV and injects data to FIWARE with configurable speed.
"""

import pandas as pd
import time
import random
from pathlib import Path
from typing import Dict, Any, Callable, Optional, List, Tuple
from collections import defaultdict
from datetime import datetime, timedelta

# Add parent path for imports
import sys
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.fiware_client import FIWAREClient

# Import STREAMS from streamlit app_config
import importlib.util
spec = importlib.util.spec_from_file_location(
    "scenarios", 
    Path(__file__).parent.parent / "streamlit" / "app_config" / "scenarios.py"
)
scenarios_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scenarios_module)
STREAMS = scenarios_module.STREAMS

# Data paths
SCENARIO_DATA_DIR = Path(__file__).parent.parent / "data" / "ola_calor_incendio"
STATE_DIR = Path(__file__).parent.parent / "streamlit" / "data"


# =============================================================================
# ENTITY MAPPING
# =============================================================================

# Map CSV column prefixes to FIWARE entity_ids
# Format: "EntityType_Instance" -> entity_id
ENTITY_IDS = {
    # Weather
    "WeatherObserved": STREAMS["WeatherObserved"]["entity_id"],
    
    # Air Quality - 3 outdoor sensors (2 Kunak TwIN Lab + 1 GobNavarra)
    "AirQualityObserved_KunakBajaNavarra": STREAMS["AirQualityObserved_KunakBajaNavarra"]["entity_id"],
    "AirQualityObserved_KunakRochapea": STREAMS["AirQualityObserved_KunakRochapea"]["entity_id"],
    "AirQualityObserved_Iturrama": STREAMS["AirQualityObserved_Iturrama"]["entity_id"],
    
    # Indoor Air Quality - 3 sensors (inBiot MICA_WELL TwIN Lab)
    "IndoorAirQuality_HUN": STREAMS["IndoorAirQuality_HUN"]["entity_id"],
    "IndoorAirQuality_inBiot": STREAMS["IndoorAirQuality_inBiot"]["entity_id"],
    "IndoorAirQuality_Itaroa": STREAMS["IndoorAirQuality_Itaroa"]["entity_id"],
    
    # Forest Fires - 3 fronts (EFFIS)
    "ForestFire_Baztan": STREAMS["ForestFire_Baztan"]["entity_id"],
    "ForestFire_Ultzama": STREAMS["ForestFire_Ultzama"]["entity_id"],
    "ForestFire_Roncal": STREAMS["ForestFire_Roncal"]["entity_id"],
    
    # Fire Forecasts - 3 predictions (TESICNOR RRD TwIN Lab)
    "FireForecast_Baztan": STREAMS["FireForecast_Baztan"]["entity_id"],
    "FireForecast_Ultzama": STREAMS["FireForecast_Ultzama"]["entity_id"],
    "FireForecast_Roncal": STREAMS["FireForecast_Roncal"]["entity_id"],
    
    # Drones - 2 units (Bravodrones TwIN Lab)
    "Drone_Fire": STREAMS["Drone_Fire"]["entity_id"],
    "Drone_Crowd": STREAMS["Drone_Crowd"]["entity_id"],
    
    # Emergency & Health
    "EmergencyCalls": STREAMS["EmergencyCalls"]["entity_id"],
    "HospitalStatus": STREAMS["HospitalStatus"]["entity_id"],
    
    # Social Media
    "SocialMediaAlert": STREAMS["SocialMediaAlert"]["entity_id"],
    
    # Traffic alerts
    "TrafficAlert_N121A": STREAMS["TrafficAlert_N121A"]["entity_id"],
    "TrafficAlert_NA411": STREAMS["TrafficAlert_NA411"]["entity_id"],
    "TrafficAlert_NA137": STREAMS["TrafficAlert_NA137"]["entity_id"],
}

# Columns that need special parsing (StructuredValue)
STRUCTURED_COLUMNS = ["SocialMediaAlert_trendingHashtags"]

# Entity types that use EntityType_Instance_attribute format in CSV
MULTI_INSTANCE_TYPES = ["AirQualityObserved", "IndoorAirQuality", "ForestFire", "FireForecast", "Drone", "TrafficAlert"]


# =============================================================================
# STAGGERED INJECTION TIMING
# =============================================================================
# Relative offset (0.0-1.0) within each tick window, reflecting natural update frequencies.
# Entities are injected in order of their offset, distributed across the tick duration.
#
# Distribution rationale:
#   0-5%   | Weather (AEMET)           | APIs lentas, actualizacion horaria
#   5-15%  | AirQuality (Kunak, Gov)   | IoT outdoor, cada minuto
#   15-25% | IndoorAirQuality (inBiot) | IoT indoor, cada minuto
#   25-40% | ForestFire (EFFIS)        | Satelite/sensores, cada 5-10 min
#   40-55% | FireForecast (TESICNOR)   | Modelos predictivos, post-fire data
#   55-70% | Emergency/Hospital        | Agregaciones en tiempo real
#   70-80% | Traffic (DGT)             | APIs gubernamentales
#   80-90% | Drones (Bravodrones)      | Telemetria continua
#   90-100%| SocialMedia               | Streaming, alta frecuencia

ENTITY_TIMING = {
    # Weather - first, slow API
    "WeatherObserved": 0.02,
    
    # Air Quality outdoor - IoT sensors, early in window
    "AirQualityObserved_KunakBajaNavarra": 0.06,
    "AirQualityObserved_KunakRochapea": 0.09,
    "AirQualityObserved_Iturrama": 0.13,
    
    # Indoor Air Quality - inBiot MICA sensors
    "IndoorAirQuality_HUN": 0.16,
    "IndoorAirQuality_inBiot": 0.19,
    "IndoorAirQuality_Itaroa": 0.23,
    
    # Forest Fires - satellite/ground sensors
    "ForestFire_Baztan": 0.27,
    "ForestFire_Ultzama": 0.32,
    "ForestFire_Roncal": 0.37,
    
    # Fire Forecasts - predictive models (after fire data)
    "FireForecast_Baztan": 0.42,
    "FireForecast_Ultzama": 0.47,
    "FireForecast_Roncal": 0.52,
    
    # Emergency services - real-time aggregations
    "EmergencyCalls": 0.57,
    "HospitalStatus": 0.64,
    
    # Traffic - government APIs
    "TrafficAlert_N121A": 0.71,
    "TrafficAlert_NA411": 0.74,
    "TrafficAlert_NA137": 0.77,
    
    # Drones - continuous telemetry
    "Drone_Fire": 0.82,
    "Drone_Crowd": 0.87,
    
    # Social Media - streaming, high frequency (last)
    "SocialMediaAlert": 0.94,
}

# Seed for deterministic jitter (same run = same timing)
STAGGER_SEED = 42


# =============================================================================
# CSV PARSER
# =============================================================================

def calculate_reopen_time(status: str, sim_time: str) -> str:
    """Calculate estimated reopen time based on status."""
    if status == "open":
        return ""
    
    # Parse sim_time (HH:MM format)
    try:
        hours, minutes = map(int, sim_time.split(":"))
        base_time = datetime(2025, 7, 6, hours, minutes)
        
        if status == "restricted":
            reopen = base_time + timedelta(hours=1)
        else:  # closed
            reopen = base_time + timedelta(hours=2)
        
        return reopen.strftime("%H:%M")
    except:
        return "indefinido"


def parse_csv_row(row: pd.Series) -> Dict[str, Dict[str, Any]]:
    """
    Parse a CSV row into FIWARE entity updates.
    
    Handles two column formats:
    - EntityType_attribute (e.g., WeatherObserved_temperature)
    - EntityType_Instance_attribute (e.g., AirQualityObserved_FelisaMunarriz_pm25)
    
    Args:
        row: Pandas Series with CSV columns
    
    Returns:
        Dict mapping entity_key to attributes dict
    """
    updates = defaultdict(dict)
    sim_time = row.get("sim_time", "09:00")
    
    # Build ISO dateObserved from sim_time (HH:MM)
    date_observed = f"2025-07-06T{sim_time}:00.000Z"
    
    for col, value in row.items():
        if col in ['t_min', 'sim_time']:
            continue
        
        if '_' not in col:
            continue
        
        # Skip if value is NaN
        if pd.isna(value):
            continue
        
        # Split column name
        parts = col.split('_')
        entity_type = parts[0]
        
        # Determine if this is a multi-instance type
        if entity_type in MULTI_INSTANCE_TYPES and len(parts) >= 3:
            # Format: EntityType_Instance_attribute
            entity_key = f"{parts[0]}_{parts[1]}"  # e.g., AirQualityObserved_FelisaMunarriz
            attribute = '_'.join(parts[2:])  # e.g., pm25 or airQualityIndex
        else:
            # Format: EntityType_attribute
            entity_key = parts[0]
            attribute = '_'.join(parts[1:])
        
        # Skip if entity not in mapping
        if entity_key not in ENTITY_IDS:
            continue
        
        # Handle StructuredValue columns (like trendingHashtags)
        if col in STRUCTURED_COLUMNS:
            if isinstance(value, str):
                hashtag_list = [h.strip() for h in value.split(',') if h.strip()]
                updates[entity_key][attribute] = {"value": hashtag_list, "type": "StructuredValue"}
            continue
        
        # Calculate estimatedReopenTime for traffic alerts
        if entity_type == "TrafficAlert" and attribute == "status":
            reopen_time = calculate_reopen_time(value, sim_time)
            updates[entity_key]["estimatedReopenTime"] = {"value": reopen_time, "type": "Text"}
        
        # Format value for FIWARE NGSI-v2
        if isinstance(value, str):
            updates[entity_key][attribute] = {"value": value, "type": "Text"}
        else:
            # Convert numpy types to native Python types for JSON serialization
            if hasattr(value, 'item'):
                value = value.item()
            updates[entity_key][attribute] = {"value": value, "type": "Number"}
    
    # Add dateObserved to all entities
    for entity_key in updates:
        updates[entity_key]["dateObserved"] = {"value": date_observed, "type": "DateTime"}
    
    return dict(updates)


# =============================================================================
# RUNNER
# =============================================================================

class ScenarioRunner:
    """Runs a scenario timeline, injecting data to FIWARE."""
    
    def __init__(self, csv_path: str, speed: float = 1.0, staggered: bool = True):
        """
        Args:
            csv_path: Path to timeline CSV
            speed: Speed multiplier (6.0 = 6x faster)
            staggered: If True, distribute entity updates across tick window
        """
        self.csv_path = Path(csv_path)
        self.speed = speed
        self.staggered = staggered
        self.client = FIWAREClient()
        self.client.refresh_token()  # Get fresh token on init
        self.running = False
        self.current_row = 0
        self.df = None
        
        # Initialize deterministic RNG for jitter
        self._rng = random.Random(STAGGER_SEED)
    
    def _calculate_delays(self, entity_keys: List[str], window_seconds: float) -> List[Tuple[str, float]]:
        """
        Calculate injection delays for entities within a tick window.
        
        Args:
            entity_keys: List of entity keys to inject
            window_seconds: Total window duration in real seconds
        
        Returns:
            List of (entity_key, delay_seconds) tuples, sorted by delay
        """
        delays = []
        for entity_key in entity_keys:
            base_offset = ENTITY_TIMING.get(entity_key, 0.5)
            # Add small deterministic jitter (±2% of window) for realism
            jitter = self._rng.uniform(-0.02, 0.02)
            final_offset = max(0.0, min(1.0, base_offset + jitter))
            delay_seconds = final_offset * window_seconds
            delays.append((entity_key, delay_seconds))
        
        # Sort by delay time
        delays.sort(key=lambda x: x[1])
        return delays
        
    def load(self):
        """Load CSV data."""
        self.df = pd.read_csv(self.csv_path)
        self.current_row = 0
        print(f"Loaded {len(self.df)} rows from {self.csv_path.name}")
    
    def inject_row(self, row_idx: int, window_seconds: float = 0.0, 
                   on_update: Optional[Callable] = None) -> Dict[str, Any]:
        """
        Inject a single row to FIWARE.
        
        Args:
            row_idx: Row index in dataframe
            window_seconds: Duration of tick window in real seconds (for staggered mode)
            on_update: Callback function(entity_type, entity_id, attributes, delay)
        
        Returns:
            Dict with t_min and sim_time
        """
        row = self.df.iloc[row_idx]
        updates = parse_csv_row(row)
        
        meta = {
            "t_min": row["t_min"],
            "sim_time": row["sim_time"]
        }
        
        if self.staggered and window_seconds > 0:
            # Calculate delays and inject with timing
            entity_keys = list(updates.keys())
            scheduled = self._calculate_delays(entity_keys, window_seconds)
            
            last_delay = 0.0
            for entity_key, delay in scheduled:
                # Wait for the incremental time since last injection
                wait_time = delay - last_delay
                if wait_time > 0:
                    time.sleep(wait_time)
                last_delay = delay
                
                entity_id = ENTITY_IDS[entity_key]
                attributes = updates[entity_key]
                
                try:
                    self.client.update_entity(entity_id, attributes)
                    if on_update:
                        on_update(entity_key, entity_id, attributes, delay)
                except Exception as e:
                    print(f"Error updating {entity_id}: {e}")
        else:
            # Original behavior: inject all at once
            for entity_key, attributes in updates.items():
                entity_id = ENTITY_IDS[entity_key]
                
                try:
                    self.client.update_entity(entity_id, attributes)
                    if on_update:
                        on_update(entity_key, entity_id, attributes, 0.0)
                except Exception as e:
                    print(f"Error updating {entity_id}: {e}")
        
        return meta
    
    def run(self, on_update: Optional[Callable] = None, on_tick: Optional[Callable] = None):
        """
        Run the full scenario.
        
        Args:
            on_update: Callback for each entity update (entity_type, entity_id, attrs, delay)
            on_tick: Callback for each time tick (t_min, sim_time)
        """
        if self.df is None:
            self.load()
        
        self.running = True
        self.current_row = 0
        
        # Reset RNG for reproducible runs
        self._rng = random.Random(STAGGER_SEED)
        
        mode_str = "staggered" if self.staggered else "burst"
        print(f"\nStarting scenario at {self.speed}x speed ({mode_str} injection)")
        print("=" * 50)
        
        last_t = 0
        
        for idx in range(len(self.df)):
            if not self.running:
                print("\nScenario stopped")
                break
            
            row = self.df.iloc[idx]
            current_t = row["t_min"]
            
            # Calculate window duration in real seconds
            # Each tick represents 15 simulated minutes
            tick_interval_min = 15  # CSV has 15-min intervals
            window_seconds = tick_interval_min * 60 / self.speed
            
            # Wait for appropriate time (adjusted by speed)
            # In staggered mode, we don't wait between ticks since injection is distributed
            wait_seconds = (current_t - last_t) * 60 / self.speed
            if not self.staggered and wait_seconds > 0 and idx > 0:
                print(f"\n... Waiting {wait_seconds:.1f}s...")
                time.sleep(wait_seconds)
            
            print(f"\n[T+{current_t}min | {row['sim_time']}]")
            
            if on_tick:
                on_tick(current_t, row["sim_time"])
            
            # Inject data (staggered mode distributes across window_seconds)
            meta = self.inject_row(idx, window_seconds, on_update)
            self.current_row = idx
            
            last_t = current_t
        
        self.running = False
        print("\n" + "=" * 50)
        print("Scenario complete")
    
    def stop(self):
        """Stop the running scenario."""
        self.running = False


# =============================================================================
# STATE FILE (for UI communication)
# =============================================================================

STATE_FILE = STATE_DIR / ".runner_state.json"

def write_state(running, t_min, sim_time, row, total_rows):
    """Write state to JSON file for UI to read."""
    import json
    with open(STATE_FILE, "w") as f:
        json.dump({
            "running": running,
            "t_min": int(t_min) if hasattr(t_min, 'item') else t_min,
            "sim_time": sim_time,
            "row": row,
            "total_rows": total_rows
        }, f)


# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run PRISMA scenario")
    parser.add_argument("scenario", choices=["15_junio", "6_julio", "1_agosto"])
    parser.add_argument("--speed", type=float, default=16.0, 
                        help="Speed multiplier (default: 16 = 15min demo for 4h scenario)")
    parser.add_argument("--no-stagger", action="store_true",
                        help="Disable staggered injection (inject all entities at once)")
    
    args = parser.parse_args()
    
    csv_path = SCENARIO_DATA_DIR / f"timeline_{args.scenario}.csv"
    
    runner = ScenarioRunner(str(csv_path), speed=args.speed, staggered=not args.no_stagger)
    runner.load()
    
    total_rows = len(runner.df)
    # Get initial values from first row
    first_row = runner.df.iloc[0]
    write_state(True, int(first_row["t_min"]), first_row["sim_time"], 0, total_rows)
    
    def on_update(entity_type, entity_id, attrs, delay):
        if runner.staggered:
            print(f"  +{delay:5.1f}s -> {entity_type}: {list(attrs.keys())}")
        else:
            print(f"  -> {entity_type}: {list(attrs.keys())}")
    
    def on_tick(t_min, sim_time):
        write_state(True, t_min, sim_time, runner.current_row, total_rows)

    try:
        runner.run(on_update=on_update, on_tick=on_tick)
    finally:
        # Use actual last row values (index is total_rows - 1)
        last_row = runner.df.iloc[-1]
        write_state(False, int(last_row["t_min"]), last_row["sim_time"], total_rows - 1, total_rows)

