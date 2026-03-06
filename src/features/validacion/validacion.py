#Defini funciones para calcular el subtotal, descuento y total final.


from decimal import Decimal

def calcular_subtotal(precio, cantidad):
    return round(Decimal(str(precio)) * Decimal(str(cantidad)), 2)

def calcular_descuento_vip(subtotal, es_vip):
    if es_vip:
        return round(Decimal(str(subtotal)) * Decimal('0.10'), 2)
    return Decimal('0.00')

def calcular_total_final(subtotal, descuento):
    return round(Decimal(str(subtotal)) - Decimal(str(descuento)), 2)