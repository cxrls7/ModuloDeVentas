# Archivo principal del sistema de registro de ventas diarias
# Este archivo contiene la función principal que inicia el programa, muestra el menú de opciones y maneja la interacción con el usuario.
import os

from src.database.conexion_mysql import obtener_conexion 
from src.features.registro.registro import registrar_venta

from src.features.historial.historial import mostrar_historial

def crear_tabla_si_no_existe():
 
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ventas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    producto VARCHAR(100) NOT NULL,
                    cantidad INT NOT NULL,
                    precio_unitario DECIMAL(12, 2) NOT NULL,
                    es_vip BOOLEAN DEFAULT FALSE,
                    subtotal DECIMAL(12, 2),
                    descuento DECIMAL(12, 2),
                    total DECIMAL(12, 2),
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conexion.commit()
        finally:
            cursor.close()
            conexion.close()

def limpiar_pantalla():
   
    os.system("clear" if os.name == "posix" else "cls") 

def linea():
    print("=" * 60)

def mostrar_bienvenida():
    limpiar_pantalla()
    linea()
    print("      --- SISTEMA DE REGISTRO DE VENTAS ---")
    linea()
    print("Bienvenido 👋")
    print("Registra ventas añadiendo descuentos para clientes VIP y consulta el historial de las ventas")
    linea()

def mostrar_menu():
    print("\n📦 MENU PRINCIPAL")
    linea()
    print("1. 📝 Registrar una venta")
    print("2. 📜 Ver historial de ventas (MySQL)")
    print("3. 🚪 Salir")
    linea() 

def main(): 
    # 1. Verificamos la base de datos antes de empezar
    crear_tabla_si_no_existe()
    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            print(">>> REGISTRO DE NUEVA VENTA")
            linea()
            registrar_venta() # Esta función ahora guarda en MySQL internamente
            input("\n✅ Presione Enter para volver al menú...")
            limpiar_pantalla()
        
        elif opcion == "2":
            limpiar_pantalla()
            print(">>> HISTORIAL DE VENTAS DESDE MYSQL")
            linea()
            mostrar_historial()
            input("\n📖 Presione Enter para volver al menú...")
            limpiar_pantalla()

        elif opcion == "3":
            linea()
            print("Gracias por utilizar el sistema. ¡Sesión finalizada! ✅")
            linea()
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
     main()
     
     
