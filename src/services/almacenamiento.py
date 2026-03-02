import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_ARCHIVO = os.path.join(BASE_DIR, "data", "ventas.json")


def obtener_ventas():
    if not os.path.exists(RUTA_ARCHIVO):
        return []

    with open(RUTA_ARCHIVO, "r") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []


def guardar_venta(venta_dict):
    ventas = obtener_ventas()  # Cargar ventas existentes

    ventas.append(venta_dict)  # Agregar nueva venta

    with open(RUTA_ARCHIVO, "w") as archivo:
        json.dump(ventas, archivo, indent=4)
