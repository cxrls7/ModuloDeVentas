#Aqui haremos las pruebas del programa antes de iniciar la interfaz gráfica, para asegurarnos de que todo funciona correctamente.
#Solo importaremos las funciones necesarias para las pruebas, no todo el programa.

import unittest
from src.features.validacion.validacion import (calcular_subtotal, calcular_descuento_vip, calcular_total_final)


class TestValidacion(unittest.TestCase):

    def test_calcular_subtotal(self):
        self.assertEqual(calcular_subtotal(10, 2), 20.00)
        self.assertEqual(calcular_subtotal(5.5, 2), 11.00)

    def test_calcular_descuento_vip(self):
        self.assertEqual(calcular_descuento_vip(100, True), 10.00)
        self.assertEqual(calcular_descuento_vip(100, False), 0.00)

    def test_total_final(self):
        self.assertEqual(calcular_total_final(100, 10), 90.00)
        self.assertEqual(calcular_total_final(50, 0), 50.00)


if __name__ == "__main__":
    unittest.main()
        