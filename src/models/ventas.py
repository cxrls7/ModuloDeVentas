#Definir la clase Venta con los atributos producto, cantidad, precio_unitario, es_vip, subtotal, descuento y total. 
# El método __init__ debe inicializar estas variables y calcular el subtotal, descuento y total utilizando las funciones definidas en validacion.py.


class Venta:
    def __init__(self, producto, cantidad, precio_unitario, es_vip):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.es_vip = es_vip

        self.subtotal = 0
        self.descuento = 0
        self.total = 0

        self.calcular_totales()  # 🔥 IMPORTANTE


    def calcular_totales(self):
        self.subtotal = self.cantidad * self.precio_unitario

        if self.es_vip:
            self.descuento = self.subtotal * 0.10
        else:
            self.descuento = 0

        self.total = self.subtotal - self.descuento