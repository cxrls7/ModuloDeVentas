import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_ARCHIVO = os.path.join(BASE_DIR, "data", "ventas.json")
def obtener_ventas():
    print("Leyendo archivo en:", RUTA_ARCHIVO)

    if not os.path.exists(RUTA_ARCHIVO):
        return []

    try:
        with open(RUTA_ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []
    

def guardar_venta(venta_dict):
    print("Venta que se va a guardar:", venta_dict)
    "Guarda una nueva venta en el archivo JSON."
    ventas = obtener_ventas()
    ventas.append(venta_dict)
    print("Ventas actuales:", ventas)

    with open(RUTA_ARCHIVO, "w") as archivo:
        json.dump(ventas, archivo, indent=4)

        

