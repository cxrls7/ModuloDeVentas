import google.generativeai as genai


genai.configure(api_key="AIzaSyDLWSGh4UWYTwAl4S72HkgbMgc57moUOnE")

def obtener_analisis_ia(producto, precio, cantidad, ventas_hoy):
   
    modelos_a_probar = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-pro']
    
    for nombre_modelo in modelos_a_probar:
        try:
            model = genai.GenerativeModel(nombre_modelo)
            prompt = f"Analiza: {cantidad} de '{producto}' a ${precio}. Responde: Eslogan | Categoría | Consejo"
            response = model.generate_content(prompt)
            
            if response and response.text:
                partes = response.text.split('|')
                if len(partes) >= 3:
                    return [p.strip() for p in partes]
                return [response.text.strip(), "General", "Venta registrada"]
        except Exception:
            continue 
            
    
    return ["¡Gracias por su compra!", "General", "IA fuera de línea"]