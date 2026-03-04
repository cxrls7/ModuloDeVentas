import google.generativeai as genai
import logging


genai.configure(api_key="TUAIzaSyDLWSGh4UWYTwAl4S72HkgbMgc57moUOnE")

def obtener_analisis_ia(producto, precio, cantidad, ventas_del_dia):
    

    try:

        model = genai.GenerativeModel('gemini-1.5-flash')
        
  
        prompt = (
            f"Analiza esta venta: {cantidad} de '{producto}' a ${precio}. "
            f"Contexto: Hoy se han hecho {ventas_del_dia} ventas antes que esta. "
            "Responde únicamente en este formato exacto separado por el símbolo '|': "
            "Eslogan para cliente | Categoría del producto | Análisis técnico para el trabajador"
        )
        
    
        response = model.generate_content(prompt)
        
        
        resultado = response.text.split('|')
        
      
        return [dato.strip() for dato in resultado]

    except Exception as e:
        
        print(f"⚠️ Error al conectar con la IA: {e}")
        return [
            "¡Gracias por su compra!", 
            "General", 
            "Sin análisis disponible en este momento."
        ]