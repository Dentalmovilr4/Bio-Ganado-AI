# 🐄 Bio-Ganado-AI: Monitor Inteligente de Ganadería

**Bio-Ganado-AI** es un ecosistema digital diseñado para el sector agropecuario, enfocado en la identificación de razas y la estimación biométrica de peso mediante Visión Artificial (Computer Vision). Este repositorio permite a los ganaderos obtener datos críticos de sus ejemplares simplemente capturando una fotografía.

---

## 🚀 Características Principales

* **Identificación de Raza:** Clasificación automática de razas (Brahman, Gyr, Angus, Holstein, etc.) mediante modelos de Deep Learning.
* **Estimación de Peso Visual:** Algoritmo basado en volumetría de píxeles para calcular el peso aproximado del animal.
* **Optimización Móvil:** Diseñado para ejecutarse en entornos ligeros y desplegarse fácilmente en plataformas web.
* **Interfaz Intuitiva:** Dashboard limpio con soporte para "Dark Mode" para facilitar la lectura en exteriores.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.10+
* **Framework de IA:** Ultralytics (YOLOv8) / TensorFlow Lite.
* **Interfaz:** Streamlit.
* **Procesamiento de Imagen:** OpenCV & Pillow.
* **Entorno de Desarrollo:** Desarrollado íntegramente en dispositivos móviles vía **Termux** y **Acode**.

---

## 📂 Estructura del Proyecto

```text
├── app.py                # Aplicación principal de Streamlit
├── models/               # Modelos .pt o .tflite entrenados
├── data/                 # Dataset de referencia biométrica
├── requirements.txt      # Dependencias del sistema
└── README.md             # Documentación del proyecto
