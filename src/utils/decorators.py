import logging
import functools


logging.basicConfig(
    filename='sistema_ventas.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def manejador_global(func):
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Guardamos el error técnico en el archivo .log para el programador
            logging.error(f"Error en {func.__name__}: {str(e)}", exc_info=True)
            # Mostramos un mensaje amigable al usuario/trabajador
            print(f"\n⚠️  [ERROR DE SISTEMA]: {e}")
            print("El incidente ha sido registrado en 'sistema_ventas.log'.")
            return None
    return envoltura