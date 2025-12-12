"""PRISMA MVP - Ola de Calor + Incendio."""
import streamlit as st

st.set_page_config(page_title="PRISMA", page_icon="🔮", layout="wide")

# =============================================================================
# SIDEBAR - Configurador escenario
# =============================================================================

with st.sidebar:
    st.title("🔮 PRISMA")
    st.caption("Ola de Calor + Incendio Forestal")
    
    st.markdown("---")
    
    # Fecha (los 3 escenarios predefinidos)
    fecha = st.radio(
        "Fecha escenario",
        ["15 Junio", "1 Julio (San Fermín)", "1 Agosto"],
        index=1  # Default: San Fermín
    )
    
    # Ubicación fija para MVP
    st.text_input("Ubicación", value="Pamplona", disabled=True)
    
    st.markdown("---")
    
    st.button("▶️ Iniciar escenario", use_container_width=True)
    st.button("⏹️ Reset", use_container_width=True)

# =============================================================================
# MAIN - Layout 3 paneles
# =============================================================================

# Mapa (mitad superior)
st.markdown("### 🗺️ Mapa")
st.container(height=300, border=True)

# Dos columnas (mitad inferior)
col_chat, col_reasoning = st.columns(2)

with col_chat:
    st.markdown("### 💬 Chat")
    st.container(height=250, border=True)

with col_reasoning:
    st.markdown("### 🧠 Razonamiento")
    st.container(height=250, border=True)
