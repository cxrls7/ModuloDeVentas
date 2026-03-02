import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_ARCHIVO = os.path.join(BASE_DIR, "data", "ventas.json")
def obtener_ventas():
    "Devuelve la lista de ventas guardadas. Si el archivo no existe o esta vacio, devuelve una lista vacia."
    if not os.path.exists(RUTA_ARCHIVO):
       return[]

    try:
        with open(RUTA_ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []
    

def guardar_venta(venta_dict):
    "Guarda una nueva venta en el archivo JSON."
    ventas = obtener_ventas()
    ventas.append(venta_dict)

    with open(RUTA_ARCHIVO, "w") as archivo:
        json.dump(ventas, archivo, indent=4)

        

