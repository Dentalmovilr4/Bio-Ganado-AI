import streamlit as st
import cv2
import numpy as np
from PIL import Image

# --- CONFIGURACIÓN ESTILO DENTALMOVILR4 ---
st.set_page_config(page_title="Bio-Ganado-AI", page_icon="🐄", layout="wide")

# Inyección de CSS para modo oscuro con acentos neón verde/lima
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    .stMetric {
        background-color: #1f2937;
        border: 1px solid #39FF14;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 0 10px #39FF14;
    }
    h1 {
        color: #39FF14;
        text-shadow: 2px 2px #000;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        background-color: #39FF14;
        color: black;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_stdio=True)

# --- CABECERA ---
st.title("🚜 BIO-GANADO AI v1.0")
st.subheader("Monitoreo Inteligente | By Dentalmovilr4")

# --- BARRA LATERAL (GUÍA) ---
with st.sidebar:
    st.header("📖 Guía de Captura")
    st.info("Para un peso exacto (+/- 5%):")
    st.markdown("""
    1. **Perfil Total:** Animal de lado.
    2. **Distancia:** 3 metros exactos.
    3. **Luz:** Evitar sombras fuertes.
    """)
    st.divider()
    st.write("🛰️ **Status:** Sistema Online")

# --- CUERPO PRINCIPAL ---
uploaded_file = st.file_uploader("📤 Sube la foto del ejemplar", type=["jpg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption='Procesando biometría...', use_container_width=True)
    
    with st.spinner('Analizando píxeles y área torácica...'):
        # Simulación de resultados (Aquí conectaremos el modelo .tflite pronto)
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.metric(label="Raza Detectada", value="Brahman Gris")
        with c2:
            st.metric(label="Clasificación", value="Macho / Adulto")
        with c3:
            st.metric(label="Peso Estimado", value="485 Kg", delta="Precisión 94%")

    st.success("✅ Análisis completado con éxito.")
else:
    st.warning("Esperando imagen para iniciar el escaneo...")

st.divider()
st.caption("© 2026 Bio-Repo-Cultivos | Innovación Agro-Digital")
