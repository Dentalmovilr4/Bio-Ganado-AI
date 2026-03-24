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

📸 Guía para una Captura Exitosa (Precisión IA)
Para que el algoritmo de Dentalmovilr4 calcule el peso con un margen de error mínimo, sigue estas 3 reglas de oro:
1. La Posición del Animal (Perfil Total)
Correcto: El animal debe estar completamente de lado (perfil), mostrando todo el largo del cuerpo desde la paleta hasta el isquion.
Incorrecto: Fotos de frente, desde atrás o en diagonal (esto distorsiona el cálculo del área visual).
2. La Distancia y el Horizonte
Distancia Fija: Se recomienda tomar la foto a una distancia de 3 metros del animal.
Nivel de la cámara: La cámara debe estar a la altura del pecho del animal, no desde muy arriba (picado) ni desde el suelo.
Suelo Plano: El animal debe estar sobre una superficie nivelada para que las patas no se "hundan" visualmente en el pasto alto.
3. La Iluminación (Sin Sombras Fuertes)
Evita fotos a mediodía con sol muy fuerte, ya que las sombras bajo el vientre pueden confundir a la IA y hacer que el animal parezca más "pesado" o "delgado" de lo que es.
Mejor hora: Temprano en la mañana o al final de la tarde.
