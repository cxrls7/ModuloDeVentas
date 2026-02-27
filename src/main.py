# Archivo principal del sistema de registro de ventas diarias
# Este archivo contiene la función principal que inicia el programa, muestra el menú de opciones y maneja la interacción con el usuario.

from src.features.registro.registro import registrar_venta
import os


def limpiar_pantalla():
    os.system("clear") 

def linea():
    print("=" * 60)


def mostrar_bienvenida():
    linea()
    print("---SISTEMA DE REGISTRO DE VENTAS DIARIAS---")
    linea()
    print("Bienvenido 👋")
    print("Este sitema permite registrar las ventas diarias de tu negocio de manera sencilla y eficiente.")
    print("Podrás ingresar los detalles de cada venta, calcular descuentos para clientes VIP")
    print("y obtener un resumen claro de cada transacción.")
    linea()
    print("EJEMPLO DE USO:")
    print("Producta: Camisa")
    print("Cantidad: 3")
    print("Precio unitario: $25.000")
    print("¿El cliente es VIP? si/no")
    linea()


def mostrar_menu():
    print("\nMENU PRINCIPAL")
    linea()
    print("1. Registrar una venta")
    print("2. Salir")
    linea() 


def despedida():
    linea()
    print("Gracias por utilizar el sistema.")
    print("Sesion finalizada correctamente ✅")
    linea()

def main(): 
    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion:").strip()

        if opcion == "1":
            limpiar_pantalla()
            print("REGISTRO DE NUEVA VENTA")
            linea()
            registrar_venta()
            input("\nPresione Enter para volver al menu")
            limpiar_pantalla()

        elif opcion == "2":
                 despedida()
                 break
        else:
            print("Opcion invalida. Intente nuevamente.\n")

if __name__ == "__main__":
     main()
     
     
