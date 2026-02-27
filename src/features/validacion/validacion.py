def calcular_subtotal(precio, cantidad):
    return round(precio * cantidad, 2)
def calcular_descuento_vip(subtotal, es_vip):
    if es_vip:
        return round(subtotal * 0.10, 2)
    return 0.0
def calcular_total_final(subtotal, descuento):
    return round(subtotal - descuento, 2)