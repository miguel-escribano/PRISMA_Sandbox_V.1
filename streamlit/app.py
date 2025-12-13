"""PRISMA MVP - Ola de Calor + Incendio."""
import sys
from pathlib import Path

# CRITICAL: Add project root to path BEFORE any imports
_this_dir = Path(__file__).resolve().parent
_project_root = _this_dir.parent
sys.path.insert(0, str(_project_root))

import streamlit as st
import subprocess
import json
import os
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from app_config.scenarios import SCENARIOS, SCENARIO_MAP, STREAMS
from app_config.knowledge_base import KNOWLEDGE_BASE

st.set_page_config(page_title="PRISMA", page_icon="🔮", layout="wide")

# =============================================================================
# STATE FILE (shared between subprocess and UI)
# =============================================================================

STATE_FILE = _this_dir / "data" / ".runner_state.json"
PID_FILE = _this_dir / "data" / ".runner_pid"

def read_runner_state():
    """Read current runner state from file."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {"running": False, "t_min": 0, "sim_time": "13:00", "row": 0, "total_rows": 0}

def is_runner_alive():
    """Check if runner subprocess is still running (Windows compatible)."""
    if not PID_FILE.exists():
        return False
    try:
        pid = int(PID_FILE.read_text().strip())
        # Windows: use tasklist to check if process exists
        result = subprocess.run(
            ["tasklist", "/FI", f"PID eq {pid}"],
            capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
        )
        return str(pid) in result.stdout
    except:
        return False

def stop_runner():
    """Stop the runner subprocess (Windows compatible)."""
    if PID_FILE.exists():
        try:
            pid = int(PID_FILE.read_text().strip())
            # Windows: use taskkill
            subprocess.run(
                ["taskkill", "/F", "/PID", str(pid)],
                capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
        except:
            pass
        PID_FILE.unlink(missing_ok=True)
    # Reset state
    with open(STATE_FILE, "w") as f:
        json.dump({"running": False, "t_min": 0, "sim_time": "13:00", "row": 0, "total_rows": 0}, f)


# Read current state from file
runner_state = read_runner_state()
runner_alive = is_runner_alive()

# If state says running but process is dead, fix it
if runner_state["running"] and not runner_alive:
    runner_state["running"] = False

with st.sidebar:
    st.title("🔮 PRISMA")
    st.caption("Ola de Calor + Incendio Forestal")
    
    st.markdown("---")
    
    fecha = st.radio(
        "Fecha escenario",
        ["15 Junio", "6 Julio (San Fermín)", "1 Agosto"],
        index=1,
        disabled=runner_state["running"]
    )
    
    st.text_input("Ubicación", value="Pamplona", disabled=True)
    
    st.markdown("---")
    
    speed = st.select_slider(
        "⏱️ Velocidad",
        options=[4, 8, 16, 32],
        value=16,
        disabled=runner_state["running"]
    )
    sim_duration = 240 // speed  # 4h simuladas
    st.caption(f"📝 {sim_duration} min demo = 4h simuladas")
    
    st.markdown("---")
    
    # Status display
    if runner_state["running"]:
        st.success(f"▶️ {runner_state['sim_time']}")
    else:
        st.info("⏸️ Detenido")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Iniciar", use_container_width=True, disabled=runner_state["running"]):
            # Map fecha to CSV file
            csv_map = {
                "15 Junio": "15_junio",
                "6 Julio (San Fermín)": "6_julio",
                "1 Agosto": "1_agosto"
            }
            scenario = csv_map[fecha]
            
            # Launch runner as subprocess (Windows compatible)
            runner_script = _this_dir / "scenario_runner.py"
            proc = subprocess.Popen(
                [sys.executable, str(runner_script), scenario, "--speed", str(speed)],
                cwd=str(_this_dir),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            
            # Save PID
            PID_FILE.write_text(str(proc.pid))
            st.rerun()
    
    with col2:
        if st.button("⏹️ Reset", use_container_width=True):
            stop_runner()
            st.rerun()

# =============================================================================
# AUTO-REFRESH (always on for simplicity)
# =============================================================================

# Always refresh every 2 seconds to catch state changes
st_autorefresh(interval=2000, limit=None, key="scenario_refresh")

# =============================================================================
# CONTEXTO DEL ESCENARIO
# =============================================================================

scenario_key = SCENARIO_MAP[fecha]
ctx = SCENARIOS[scenario_key]

# =============================================================================
# MAIN - Tabs
# =============================================================================

tab_main, tab_scenario, tab_domain, tab_cascades = st.tabs(["📊 Vista Principal", "📡 Escenario", "📚 Dominio", "🔗 Cascadas"])

# -----------------------------------------------------------------------------
# TAB 1: Vista Principal
# -----------------------------------------------------------------------------
with tab_main:
    st.caption("🗺️ Mapa")
    st.container(height=350, border=True)
    
    col_chat, col_reasoning = st.columns(2)
    
    with col_chat:
        st.caption("💬 Chat")
        st.container(height=180, border=True)
    
    with col_reasoning:
        st.caption("🧠 Razonamiento")
        st.container(height=180, border=True)

# -----------------------------------------------------------------------------
# TAB 2: Escenario - Timeline CSV + Progress
# -----------------------------------------------------------------------------
with tab_scenario:
    # Map to CSV file
    csv_map = {
        "15 Junio": "timeline_15_junio.csv",
        "6 Julio (San Fermín)": "timeline_6_julio.csv",
        "1 Agosto": "timeline_1_agosto.csv"
    }
    csv_file = _this_dir / "data" / csv_map[fecha]
    
    # --- BIG TIME DISPLAY ---
    col_time, col_status = st.columns([2, 1])
    with col_time:
        sim_time = runner_state.get("sim_time", "13:00")
        st.markdown(f"## 🕐 {sim_time}")
        st.caption("Hora del escenario (6 julio 2025)")
    
    with col_status:
        if runner_state["running"]:
            st.success("▶️ EN EJECUCIÓN")
        else:
            st.info("⏸️ DETENIDO")
    
    # --- PROGRESS BAR ---
    total_rows = runner_state.get("total_rows", 1) or 1
    current_row = runner_state.get("row", 0)
    progress = current_row / total_rows if total_rows > 0 else 0
    st.progress(progress, text=f"Tick {current_row} / {total_rows}")
    
    st.markdown("---")
    
    # --- CSV DATA ---
    st.markdown("### 📊 Timeline del Escenario")
    
    if csv_file.exists():
        df = pd.read_csv(csv_file)
        
        # Highlight current row
        def highlight_row(row):
            if row.name == current_row:
                return ['background-color: #264653; color: white'] * len(row)
            return [''] * len(row)
        
        # Show dataframe with styling
        st.dataframe(
            df.style.apply(highlight_row, axis=1),
            use_container_width=True,
            height=400
        )
        
        st.caption(f"📁 {csv_file.name} | {len(df)} filas | {len(df.columns)} columnas")
    else:
        st.warning(f"CSV no encontrado: {csv_file}")

# -----------------------------------------------------------------------------
# TAB 3: Knowledge Base
# -----------------------------------------------------------------------------
with tab_domain:
    st.markdown("### 📚 Knowledge Base del Agente")
    st.caption("Información estática que el LLM usa para razonar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("🏥 Infraestructura Crítica", expanded=True):
            st.json(KNOWLEDGE_BASE["infraestructura_critica"])
        
        with st.expander("⚠️ Umbrales de Alerta", expanded=True):
            st.json(KNOWLEDGE_BASE["umbrales_alerta"])
        
        with st.expander("🗺️ Geografía", expanded=True):
            st.json(KNOWLEDGE_BASE["geografia"])
        
        with st.expander("📡 Fuentes de Datos", expanded=False):
            for k, v in KNOWLEDGE_BASE["fuentes_datos"].items():
                st.markdown(f"- **{k}**: {v}")
    
    with col2:
        with st.expander("✅ Acciones Disponibles", expanded=True):
            for a in KNOWLEDGE_BASE["acciones_disponibles"]:
                st.markdown(f"- **{a['accion']}** → {a['responsable']}")
        
        with st.expander("👥 Stakeholders", expanded=True):
            for k, v in KNOWLEDGE_BASE["stakeholders"].items():
                st.markdown(f"- **{k}**: {v}")
        
        with st.expander("📋 Protocolos", expanded=True):
            for k, v in KNOWLEDGE_BASE["protocolos"].items():
                st.markdown(f"- **{k}**: {v}")

# -----------------------------------------------------------------------------
# TAB 4: Cascadas (Few-shot)
# -----------------------------------------------------------------------------
with tab_cascades:
    st.markdown("### 🔗 Cascadas Típicas (Few-shot para LLM)")
    st.caption("Ejemplos de razonamiento que guían al agente")
    
    for i, cascade in enumerate(KNOWLEDGE_BASE["cascadas_tipicas"]):
        with st.expander(f"**{cascade['trigger']}**", expanded=True):
            if "inferencia" in cascade:
                st.info(f"💡 Inferencia: {cascade['inferencia']}")
            st.markdown("**Cascada:**")
            for step in cascade["cascada"]:
                st.markdown(f"  → {step}")
            st.warning(f"⏱️ Ventana de acción: {cascade['ventana_accion']}")
