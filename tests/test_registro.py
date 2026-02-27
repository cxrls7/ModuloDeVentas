#Este es el test de registro, se encarga de probar el proceso de registro de un nuevo usuario en la aplicación. 
#Importare como en el de validacion solo las funciones necesarias para las pruebas, no todo el programa.

import unittest
from src.models.ventas import Venta


class TestRegistro(unittest.TestCase):

    def test_creacion_venta(self):
        venta = venta("Camisa", 2, 25.0, True)

        self.assertEqual(venta.producto, "Camisa")
        self.assertEqual(venta.cantidad, 2)
        self.assertEqual(venta.precio_unitario, 25.0)
        self.assertTrue(venta.es_vip)


if __name__ == "__main__":
    unittest.main()


        