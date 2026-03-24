import cv2
from ultralytics import YOLO

def probar_deteccion():
    print("🚀 Iniciando Motor de IA Bio-Ganado...")
    
    # Cargamos un modelo base (YOLOv8n es el más ligero para móvil)
    try:
        model = YOLO('yolov8n.pt') 
        print("✅ Modelo cargado correctamente.")
        
        # Aquí simulamos la entrada de imagen
        print("📸 Buscando ganado en la escena...")
        
        # Nota: 'cow' es la clase 19 en el dataset COCO por defecto de YOLO
        # Este comando imprimirá si detecta algo en una imagen de prueba
        results = model.predict(source='https://ultralytics.com/images/bus.jpg', save=False)
        
        print("--- RESULTADOS DEL TEST ---")
        for result in results:
            print(f"Detecciones encontradas: {len(result.boxes)}")
            
        print("\n🔥 ¡Prueba exitosa! El entorno está listo para Bio-Ganado-AI.")
        
    except Exception as e:
        print(f"❌ Error en el test: {e}")

if __name__ == "__main__":
    probar_deteccion()
