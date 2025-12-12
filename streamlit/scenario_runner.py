"""
PRISMA MVP - Scenario Runner
Reads timeline CSV and injects data to FIWARE with configurable speed.
"""

import pandas as pd
import time
from pathlib import Path
from typing import Dict, Any, Callable, Optional
from collections import defaultdict

# Add parent to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.fiware_client import FIWAREClient
from streamlit.config.scenarios import STREAMS


# =============================================================================
# ENTITY MAPPING
# =============================================================================

# Map CSV column prefixes to FIWARE entity_ids
ENTITY_IDS = {
    "WeatherObserved": STREAMS["WeatherObserved"]["entity_id"],
    "AirQualityObserved": STREAMS["AirQualityObserved"]["entity_id"],
    "ForestFire": STREAMS["ForestFire"]["entity_id"],
    "EmergencyCalls112": STREAMS["EmergencyCalls112"]["entity_id"],
    "HospitalOccupancy": STREAMS["HospitalOccupancy"]["entity_id"],
    "SocialMediaAlert": STREAMS["SocialMediaAlert"]["entity_id"],
}


# =============================================================================
# CSV PARSER
# =============================================================================

def parse_csv_row(row: pd.Series) -> Dict[str, Dict[str, Any]]:
    """
    Parse a CSV row into FIWARE entity updates.
    
    Args:
        row: Pandas Series with columns like 'WeatherObserved_temperature'
    
    Returns:
        Dict mapping entity_type to attributes dict
    """
    updates = defaultdict(dict)
    
    for col, value in row.items():
        if col in ['t_min', 'sim_time']:
            continue
        
        if '_' not in col:
            continue
        
        # Parse EntityType_attribute format
        parts = col.split('_', 1)
        if len(parts) != 2:
            continue
        
        entity_type, attribute = parts
        
        if entity_type not in ENTITY_IDS:
            continue
        
        # Format value for FIWARE NGSI-v2
        if isinstance(value, str):
            updates[entity_type][attribute] = {"value": value, "type": "Text"}
        elif pd.isna(value):
            continue
        else:
            updates[entity_type][attribute] = {"value": value, "type": "Number"}
    
    return dict(updates)


# =============================================================================
# RUNNER
# =============================================================================

class ScenarioRunner:
    """Runs a scenario timeline, injecting data to FIWARE."""
    
    def __init__(self, csv_path: str, speed: float = 1.0):
        """
        Args:
            csv_path: Path to timeline CSV
            speed: Speed multiplier (6.0 = 6x faster)
        """
        self.csv_path = Path(csv_path)
        self.speed = speed
        self.client = FIWAREClient()
        self.running = False
        self.current_row = 0
        self.df = None
        
    def load(self):
        """Load CSV data."""
        self.df = pd.read_csv(self.csv_path)
        self.current_row = 0
        print(f"Loaded {len(self.df)} rows from {self.csv_path.name}")
        
    def create_entities(self):
        """Create FIWARE entities if they don't exist."""
        for entity_type, entity_id in ENTITY_IDS.items():
            stream_config = STREAMS[entity_type]
            location = stream_config.get("location", {})
            
            entity_data = {
                "id": entity_id,
                "type": entity_type,
            }
            
            # Add location if available
            if location:
                entity_data["location"] = {
                    "type": "geo:json",
                    "value": {
                        "type": "Point",
                        "coordinates": [location["lon"], location["lat"]]
                    }
                }
            
            # Add initial attributes with empty values
            for attr_name, attr_config in stream_config["attributes"].items():
                if attr_config["type"] == "Text":
                    entity_data[attr_name] = {"type": "Text", "value": ""}
                else:
                    entity_data[attr_name] = {"type": "Number", "value": 0}
            
            try:
                self.client.create_entity(entity_data)
                print(f"  Created: {entity_id}")
            except Exception as e:
                if "Already Exists" in str(e) or "422" in str(e):
                    print(f"  Exists: {entity_id}")
                else:
                    print(f"  Error creating {entity_id}: {e}")
    
    def inject_row(self, row_idx: int, on_update: Optional[Callable] = None) -> Dict[str, Any]:
        """
        Inject a single row to FIWARE.
        
        Args:
            row_idx: Row index in dataframe
            on_update: Callback function(entity_type, entity_id, attributes)
        
        Returns:
            Dict with t_min and sim_time
        """
        row = self.df.iloc[row_idx]
        updates = parse_csv_row(row)
        
        meta = {
            "t_min": row["t_min"],
            "sim_time": row["sim_time"]
        }
        
        for entity_type, attributes in updates.items():
            entity_id = ENTITY_IDS[entity_type]
            
            try:
                self.client.update_entity(entity_id, attributes)
                if on_update:
                    on_update(entity_type, entity_id, attributes)
            except Exception as e:
                print(f"Error updating {entity_id}: {e}")
        
        return meta
    
    def run(self, on_update: Optional[Callable] = None, on_tick: Optional[Callable] = None):
        """
        Run the full scenario.
        
        Args:
            on_update: Callback for each entity update
            on_tick: Callback for each time tick (t_min, sim_time)
        """
        if self.df is None:
            self.load()
        
        self.running = True
        self.current_row = 0
        
        print(f"\nStarting scenario at {self.speed}x speed")
        print("=" * 50)
        
        last_t = 0
        
        for idx in range(len(self.df)):
            if not self.running:
                print("\nScenario stopped")
                break
            
            row = self.df.iloc[idx]
            current_t = row["t_min"]
            
            # Wait for appropriate time (adjusted by speed)
            wait_seconds = (current_t - last_t) * 60 / self.speed
            if wait_seconds > 0 and idx > 0:
                print(f"\n⏳ Waiting {wait_seconds:.1f}s...")
                time.sleep(wait_seconds)
            
            # Inject data
            meta = self.inject_row(idx, on_update)
            self.current_row = idx
            
            print(f"\n[T+{meta['t_min']}min | {meta['sim_time']}]")
            
            if on_tick:
                on_tick(meta["t_min"], meta["sim_time"])
            
            last_t = current_t
        
        self.running = False
        print("\n" + "=" * 50)
        print("Scenario complete")
    
    def stop(self):
        """Stop the running scenario."""
        self.running = False


# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run PRISMA scenario")
    parser.add_argument("scenario", choices=["15_junio", "6_julio", "1_agosto"])
    parser.add_argument("--speed", type=float, default=6.0, help="Speed multiplier")
    parser.add_argument("--create-entities", action="store_true", help="Create FIWARE entities first")
    
    args = parser.parse_args()
    
    csv_path = Path(__file__).parent / "data" / f"timeline_{args.scenario}.csv"
    
    runner = ScenarioRunner(str(csv_path), speed=args.speed)
    runner.load()
    
    if args.create_entities:
        print("\nCreating FIWARE entities...")
        runner.create_entities()
    
    def on_update(entity_type, entity_id, attrs):
        print(f"  → {entity_type}: {list(attrs.keys())}")
    
    runner.run(on_update=on_update)

