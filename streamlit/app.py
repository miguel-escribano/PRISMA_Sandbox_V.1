"""PRISMA MVP - Ola de Calor + Incendio."""
import streamlit as st
from config.scenarios import SCENARIOS, SCENARIO_MAP, STREAMS
from config.knowledge_base import KNOWLEDGE_BASE

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
        ["15 Junio", "6 Julio (San Fermín)", "1 Agosto"],
        index=1
    )
    
    st.text_input("Ubicación", value="Pamplona", disabled=True)
    
    st.markdown("---")
    
    speed = st.select_slider(
        "⏱️ Velocidad",
        options=[1, 2, 4, 6, 10, 20],
        value=6
    )
    sim_duration = 180 // speed  # 3h simuladas
    st.caption(f"📝 {sim_duration} min demo = 3h simuladas")
    
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
# TAB 2: Contexto + Streams
# -----------------------------------------------------------------------------
with tab_scenario:
    # Contexto
    st.markdown("### 📋 Contexto del Escenario")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Población", f"{ctx['poblacion']:,}")
    with col2:
        st.metric("Cap. Operativa", f"{ctx['capacidad_operativa_pct']}%")
    with col3:
        st.metric("Tensión política", ctx['contexto_politico'])
    with col4:
        st.metric("Velocidad fuego", f"x{ctx['fire_spread_multiplier']}")
    
    st.caption(ctx["narrativa"])
    
    st.markdown("---")
    
    # Streams
    st.markdown("### 📡 Streams de Datos → FIWARE")
    
    for stream_name, stream_config in STREAMS.items():
        loc = stream_config.get("location", {})
        loc_str = f"📍 {loc.get('name', '')} ({loc.get('lat', '')}, {loc.get('lon', '')})"
        dist = stream_config.get("distance_to_pamplona_km")
        if dist:
            loc_str += f" — {dist}km de Pamplona"
        
        with st.expander(f"**{stream_name}** — {loc.get('name', '')}", expanded=True):
            st.caption(loc_str)
            cols = st.columns(len(stream_config["attributes"]))
            for i, (attr_name, attr_config) in enumerate(stream_config["attributes"].items()):
                with cols[i % len(cols)]:
                    unit = attr_config.get("unit", "")
                    st.caption(attr_name)
                    st.code(f"-- {unit}")

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
