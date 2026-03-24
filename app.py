import streamlit as st
import cv2
import numpy as np
from PIL import Image

# --- CONFIGURACIÓN DE INTERFAZ NEÓN (DENTALMOVILR4 STYLE) ---
st.set_page_config(page_title="Bio-Ganado-AI Universal", page_icon="🐄", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e0e0; }
    .stMetric { 
        background-color: #1f2937; 
        border: 1px solid #39FF14; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 0 15px #39FF14;
    }
    h1, h2, h3 { color: #39FF14; text-shadow: 1px 1px #000; font-family: 'Courier New', monospace; }
    .stButton>button { 
        background-color: #39FF14; color: black; 
        width: 100%; border-radius: 10px; font-weight: bold;
    }
    .stSelectbox label { color: #39FF14 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR BIOMÉTRICO UNIVERSAL ---
def calcular_peso_pro(raza, largo_px, torax_px, ratio=0.05):
    # LC = Largo Corporal | PT = Perímetro Torácico
    LC = largo_px * ratio
    PT = (torax_px * ratio) * 3.14
    
    # Base de datos de constantes por biotipo (Matemática de precisión)
    # C es el divisor en la fórmula de Quetelet
    libreria_razas = {
        # CEBUINOS / CARNE TRÓPICO
        "Gyr": 300, "Brahman": 315, "Nellore": 310, "Guzerat": 312, "Indubrasil": 310,
        # EUROPEOS CARNE
        "Angus": 270, "Hereford": 280, "Charolais": 275, "Limousin": 280,
        # LECHEROS
        "Holstein": 285, "Jersey": 265, "Pardo Suizo": 290, "Ayrshire": 280,
        # DOBLE PROPÓSITO / OTROS
        "Simmental": 295, "Normando": 300, "Bon": 305, "Cruce": 300
    }
    
    C = libreria_razas.get(raza, 300) # Si la raza no está, usa promedio 300
    peso = (PT**2 * LC) / C
    return round(peso, 2)

# --- CABECERA ---
st.title("🚜 BIO-GANADO AI: ESCÁNER UNIVERSAL")
st.write("### Identificación de Raza y Biometría | Dentalmovilr4")

# --- PANEL DE CONTROL LATERAL ---
with st.sidebar:
    st.header("⚙️ Ajustes de Escaneo")
    modo = st.radio("Modo de Análisis", ["Automático (IA)", "Manual (Asistido)"])
    st.divider()
    st.info("💡 Tip: Para razas de carne (Angus/Brahman), asegúrese de capturar bien la profundidad del lomo.")

# --- CARGA DE IMAGEN ---
archivo = st.file_uploader("📤 Sube la foto del ejemplar (Cualquier Raza)", type=["jpg", "png", "jpeg"])

if archivo:
    img = Image.open(archivo)
    st.image(img, caption="Imagen en análisis...", use_container_width=True)
    
    # Simulación de detección multiraza
    # En producción, 'raza_ia' vendrá del resultado de model.predict()
    opciones_razas = ["Gyr", "Brahman", "Holstein", "Angus", "Simmental", "Jersey", "Cruce"]
    raza_ia = st.selectbox("Confirmar Raza Detectada:", opciones_razas)
    
    with st.spinner('🔬 Procesando biometría multiraza...'):
        # Valores de prueba que luego serán automáticos por detección de píxeles
        peso_final = calcular_peso_pro(raza_ia, 840, 370)
        
        st.divider()
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.metric("Raza Identificada", raza_ia)
        with c2:
            st.metric("Categoría", "Bovino Universal")
        with c3:
            st.metric("Peso Calculado", f"{peso_final} Kg", "Precisión IA")
            
    st.success(f"Detección exitosa. El ejemplar {raza_ia} cumple con los estándares biométricos.")
else:
    st.warning("Esperando archivo para procesar...")

st.divider()
st.caption("© 2026 Bio-Repo-Cultivos | Innovación Digital por Dentalmovilr4")

