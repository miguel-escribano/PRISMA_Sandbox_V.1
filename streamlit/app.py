"""PRISMA MVP - Ola de Calor + Incendio."""
import streamlit as st
from config.scenarios import SCENARIOS, SCENARIO_MAP, STREAMS

st.set_page_config(page_title="PRISMA", page_icon="🔮", layout="wide")

# =============================================================================
# SESSION STATE
# =============================================================================

if "scenario_running" not in st.session_state:
    st.session_state.scenario_running = False

# =============================================================================
# SIDEBAR - Configurador escenario
# =============================================================================

with st.sidebar:
    st.title("🔮 PRISMA")
    st.caption("Ola de Calor + Incendio Forestal")
    
    st.markdown("---")
    
    fecha = st.radio(
        "Fecha escenario",
        ["15 Junio", "1 Julio (San Fermín)", "1 Agosto"],
        index=1
    )
    
    st.text_input("Ubicación", value="Pamplona", disabled=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Iniciar", use_container_width=True):
            st.session_state.scenario_running = True
    with col2:
        if st.button("⏹️ Reset", use_container_width=True):
            st.session_state.scenario_running = False

# =============================================================================
# CONTEXTO DEL ESCENARIO
# =============================================================================

scenario_key = SCENARIO_MAP[fecha]
ctx = SCENARIOS[scenario_key]

# =============================================================================
# MAIN - Tabs
# =============================================================================

tab_main, tab_data = st.tabs(["📊 Vista Principal", "📡 Contexto & Streams"])

# -----------------------------------------------------------------------------
# TAB 1: Vista Principal
# -----------------------------------------------------------------------------
with tab_main:
    st.markdown("### 🗺️ Mapa")
    st.container(height=250, border=True)
    
    col_chat, col_reasoning = st.columns(2)
    
    with col_chat:
        st.markdown("### 💬 Chat")
        st.container(height=200, border=True)
    
    with col_reasoning:
        st.markdown("### 🧠 Razonamiento")
        st.container(height=200, border=True)

# -----------------------------------------------------------------------------
# TAB 2: Contexto + Streams
# -----------------------------------------------------------------------------
with tab_data:
    # Contexto
    st.markdown("### 📋 Contexto del Escenario")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Población", f"{ctx['poblacion']:,}")
    with col2:
        st.metric("Hospital", f"{ctx['hospital_capacity_pct']}%")
    with col3:
        st.metric("Tensión política", ctx['contexto_politico'])
    with col4:
        st.metric("Velocidad fuego", f"x{ctx['fire_spread_multiplier']}")
    
    st.caption(ctx["narrativa"])
    
    st.markdown("---")
    
    # Streams
    st.markdown("### 📡 Streams de Datos → FIWARE")
    
    if not st.session_state.scenario_running:
        st.info("Inicia el escenario para ver los streams")
    else:
        for stream_name, stream_config in STREAMS.items():
            with st.expander(f"**{stream_name}** ({stream_config['entity_id']})", expanded=True):
                cols = st.columns(len(stream_config["attributes"]))
                for i, (attr_name, attr_config) in enumerate(stream_config["attributes"].items()):
                    with cols[i % len(cols)]:
                        unit = attr_config.get("unit", "")
                        st.metric(attr_name, f"--{unit}")
