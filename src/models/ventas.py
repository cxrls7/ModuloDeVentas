#Definir la clase Venta con los atributos producto, cantidad, precio_unitario, es_vip, subtotal, descuento y total. 
# El método __init__ debe inicializar estas variables y calcular el subtotal, descuento y total utilizando las funciones definidas en validacion.py.


from decimal import Decimal

class Venta:
    def __init__(self, producto, cantidad, precio_unitario, es_vip, 
                 subtotal=None, descuento=None, total=None,
                 categoria="General", eslogan_ia="", feedback_interno=""):
        
        self.producto = producto
        self.cantidad = Decimal(str(cantidad))
        self.precio_unitario = Decimal(str(precio_unitario))
        self.es_vip = es_vip
        
       
        self.subtotal = Decimal(str(subtotal)) if subtotal is not None else Decimal('0.00')
        self.descuento = Decimal(str(descuento)) if descuento is not None else Decimal('0.00')
        self.total = Decimal(str(total)) if total is not None else Decimal('0.00')
        
        
        self.categoria = categoria
        self.eslogan_ia = eslogan_ia
        self.feedback_interno = feedback_interno