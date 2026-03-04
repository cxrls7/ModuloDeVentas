from reportlab.pdfgen import canvas 
from datetime import datetime

def generar_ticket_pdf(venta):
    nombre_archivo = f"ticket_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(nombre_archivo)

    c.setFont("Helvetica_bold", 16)
    c.drawString(100, 750, "TICKET DE VENTA - MI NEGOCIO")

    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(100, 700, f"Producto: {venta.producto}")
    c.drawString(100, 680, f"Cantidad: {venta.cantidad}")
    c.drawString(100, 660, f"Total: ${venta.total}")
    
    c.save()
    print(f"✅ Ticket generado: {nombre_archivo}")
    