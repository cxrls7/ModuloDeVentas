# Archivo principal del sistema de registro de ventas diarias
# Este archivo contiene la función principal que inicia el programa, muestra el menú de opciones y maneja la interacción con el usuario.
import os
from src.database.conexion_mysql import obtener_conexion 
from src.features.registro.registro import registrar_venta
from src.features.historial.historial import mostrar_historial
from src.database.queries import obtener_dashboard_trabajador
from src.utils.decorators import manejador_global

def crear_tabla_si_no_existe():
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            # Actualizado para incluir las columnas de la IA
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
                    categoria VARCHAR(50),
                    eslogan_ia TEXT,
                    feedback_interno TEXT,
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
    print("      --- SISTEMA DE GESTIÓN INTELIGENTE ---")
    linea()
    print("Bienvenido 👋 ")
    linea()

def mostrar_menu():
    print("\n📦 MENU PRINCIPAL")
    linea()
    print("1. 📝 Registrar una venta ")
    print("2. 📜 Ver historial de ventas (MySQL)")
    print("3. 📊 Panel de Control")
    print("4. 🚪 Salir")
    linea() 


def ejecutar_dashboard():
    limpiar_pantalla()
    print(">>> PANEL DE CONTROL DEL TRABAJADOR")
    linea()
    
    ventas_hoy, ganancia_hoy = obtener_dashboard_trabajador()
    
    
    total_dinero = ganancia_hoy if ganancia_hoy else 0.0
    
    print(f"📈 Ventas realizadas hoy: {ventas_hoy}")
    print(f"💰 Recaudación total:     ${total_dinero:.2f}")
    linea()
    print("Consejo: Revisa el log de errores si notas discrepancias.")
    input("\n✅ Presione Enter para volver al menú...")
    limpiar_pantalla()

def main(): 
    crear_tabla_si_no_existe()
    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            print(">>> REGISTRO DE NUEVA VENTA")
            linea()
          
            registrar_venta() 
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
            ejecutar_dashboard()

        elif opcion == "4":
            linea()
            print("Gracias por utilizar el sistema. ¡Sesión finalizada! ✅")
            linea()
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
     main()
     
