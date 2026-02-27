#Este módulo se encarga de registrar las ventas, calcular el subtotal, descuento y total final, y mostrar un resumen de la venta
#Importe las funciones necesarias para el registro de ventas y los cálculos relacionados
#Importe tambien la clase venta para crear objetos de venta y almacenar los detalles de cada transacción


from src.models.ventas import ventas
from src.features.validacion.validacion import(calcular_subtotal,calcular_descuento_vip,calcular_total_final)


def registrar_venta():
    producto = input("Ingrese el nombre del producto:").strip()

    try:
        cantidad = int(input("Ingrese la cantidad:"))
        precio = float(input("Ingrese el precio unitario:"))
    except ValueError:
        print("Error‼️: Debe ingresar valores numericos validos.")
        return
    if cantidad <= 0 or precio <= 0:
        print("Error‼️: La cantidad y el precio deben ser mayores a 0.")
        return 
    
    while True:
        vip_input = input("¿El cliente es VIP? si/no)").strip().lower()
        if vip_input in ["si", "no"]:
            es_vip = vip_input == "si"
            break
        else:
            print("Error‼️: Por favor ingrese 'si' o 'no'.")

    venta = venta(producto, cantidad, precio, es_vip)

    venta.subtotal = calcular_subtotal(venta.precio_unitario, venta.cantidad)
    venta.descuento = calcular_descuento_vip(venta.subtotal , venta.es_vip)
    venta.total = calcular_total_final(venta.subtotal, venta.descuento)

    mostrar_resumen_venta(venta)


def mostrar_resumen_venta(venta):
    print("\n" + "-" * 60) 
    print ("             RESUMEN DE LA VENTA")
    print("-" * 60) 
    print(f"Producto        : {venta.producto}")
    print(f"Cantidad        : {venta.cantidad}")
    print(f"Precio Unitario : ${venta.precio_unitario:.2f}") 
    print("-" * 60)
    print(f"Subtotal        : ${venta.subtotal:.2f}")
    print(f"Descuento VIP   : ${venta.descuento:.2f}")
    print("-" * 60)
    print(f"TOTAL A PAGAR   : ${venta.total:.2f}")
    print("-" * 60)

          
         

