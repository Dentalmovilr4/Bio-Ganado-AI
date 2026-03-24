import streamlit as st
import cv2
import numpy as np
from PIL import Image
from datetime import datetime

# --- CONFIGURACIÓN DE INTERFAZ ESTILO DENTALMOVILR4 ---
st.set_page_config(page_title="Bio-Ganado AI Universal", page_icon="🐄", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e0e0; }
    .stMetric { 
        background-color: #1f2937; border: 1px solid #39FF14; 
        padding: 15px; border-radius: 12px; box-shadow: 0 0 10px #39FF14;
    }
    h1, h2, h3 { color: #39FF14; font-family: 'Courier New', monospace; text-shadow: 2px 2px #000; }
    .stButton>button { 
        background-color: #39FF14; color: black; font-weight: bold; 
        width: 100%; border-radius: 8px; border: none;
    }
    .historial-card {
        background-color: #161b22; border: 1px solid #30363d;
        padding: 15px; margin-bottom: 20px; border-radius: 10px;
    }
    .fecha-badge {
        background-color: #39FF14; color: black;
        padding: 4px 10px; border-radius: 5px; font-weight: bold; font-size: 0.85rem;
    }
    .info-raza { color: #39FF14; font-weight: bold; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE RAZAS Y CONSTANTES (C) ---
# Cubre carne, leche, doble propósito y criollas
DATABASE_RAZAS = {
    "CEBUINAS": {"Gyr": 300, "Brahman": 315, "Nellore": 310, "Guzerat": 312},
    "EUROPEAS CARNE": {"Angus": 270, "Hereford": 280, "Charolais": 275, "Limousin": 280},
    "EUROPEAS LECHE": {"Holstein": 285, "Jersey": 265, "Pardo Suizo": 290},
    "CRIOLLAS / MEZCLAS": {"BON": 305, "Sinuano": 310, "Hartón": 300, "Cruce/7 Colores": 300}
}

# --- INICIALIZAR EL HISTORIAL EN LA SESIÓN ---
if 'historial_ganado' not in st.session_state:
    st.session_state.historial_ganado = []

# --- MOTOR DE CÁLCULO BIOMÉTRICO ---
def calcular_peso_universal(c_raza, largo_px, torax_px, ratio=0.05):
    # Simulación de conversión píxel -> metro y fórmula de Quetelet
    largo_m = largo_px * ratio
    torax_m = (torax_px * ratio) * 3.14
    peso_est = (torax_m**2 * largo_m) / c_raza
    return round(peso_est, 2)

# --- ESTRUCTURA DE LA APP ---
st.title("🚜 BIO-GANADO AI: GESTIÓN UNIVERSAL")
col_izq, col_der = st.columns([2, 1])

with col_izq:
    st.write("### 📸 Análisis de Nuevo Ejemplar")
    archivo = st.file_uploader("Sube la foto del animal", type=["jpg", "png", "jpeg"])
    
    if archivo:
        img_original = Image.open(archivo)
        st.image(img_original, caption="Imagen cargada", use_container_width=True)
        
        # Selección de Raza para el cálculo
        c1, c2 = st.columns(2)
        with c1:
            cat_escogida = st.selectbox("Categoría:", list(DATABASE_RAZAS.keys()))
        with c2:
            raza_escogida = st.selectbox("Raza Detectada:", list(DATABASE_RAZAS[cat_escogida].keys()))
        
        if st.button("⚖️ ANALIZAR, PESAR Y GUARDAR"):
            # Obtenemos la constante de la raza y calculamos
            constante = DATABASE_RAZAS[cat_escogida][raza_escogida]
            peso_final = calcular_peso_universal(constante, 850, 375) # Datos simulación IA
            
            # Captura de fecha y hora actual
            fecha_actual = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
            
            # Guardamos en la lista de historial
            registro = {
                "fecha": fecha_actual,
                "raza": raza_escogida,
                "peso": peso_final,
                "foto": img_original
            }
            st.session_state.historial_ganado.insert(0, registro)
            st.success(f"¡Ejemplar {raza_escogida} guardado exitosamente!")

with col_der:
    st.write("### 📜 Historial de Registros")
    if not st.session_state.historial_ganado:
        st.info("Aún no hay pesajes grabados hoy.")
    else:
        for item in st.session_state.historial_ganado:
            with st.container():
                st.markdown(f"""
                <div class="historial-card">
                    <span class="fecha-badge">📅 {item['fecha']}</span><br><br>
                    Raza: <span class="info-raza">{item['raza']}</span><br>
                    Peso: <span style="color:#39FF14; font-size:1.3rem; font-weight:bold;">{item['peso']} Kg</span>
                </div>
                """, unsafe_allow_html=True)
                st.image(item['foto'], width=220)
                st.divider()

st.divider()
st.caption("© 2026 Bio-Repo-Cultivos | Innovación Digital por Dentalmovilr4")


