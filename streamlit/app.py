"""PRISMA MVP - Layout skeleton."""
import streamlit as st

st.set_page_config(page_title="PRISMA", page_icon="🔮", layout="wide")

# =============================================================================
# SIDEBAR - Configurador escenarios
# =============================================================================

with st.sidebar:
    st.title("🔮 PRISMA")
    st.caption("Configurador de escenarios")
    
    # Caso
    caso = st.radio("Caso", ["🌡️ Ola Calor + Incendio", "🔐 Ciberataque Agua"])
    
    st.markdown("---")
    
    # Parámetros básicos
    st.markdown("**Contexto**")
    ubicacion = st.text_input("Ubicación", value="Pamplona")
    fecha = st.date_input("Fecha")
    hora = st.time_input("Hora inicio")
    
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

