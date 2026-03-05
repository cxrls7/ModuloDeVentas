import google.generativeai as genai


genai.configure(api_key="AIzaSyDLWSGh4UWYTwAl4S72HkgbMgc57moUOnE")

def obtener_analisis_ia(producto, precio, cantidad, ventas_hoy):
    
    try:
        
        model = genai.GenerativeModel('gemini-1.5-flash')
        
     
        prompt = f"""
        Actúa como un analista de inventario y ventas para un comercio en Colombia.
        DATOS DE VENTA:
        - Producto: {producto}
        - Precio Unitario: ${precio} COP
        - Cantidad Vendida: {cantidad}
        
        Genera un análisis técnico estrictamente en este formato de una sola línea (separa con |):
        Resumen de la operación | Categoría funcional | Acción de negocio sugerida
        
        RESTRICCIONES:
        1. NO uses eslóganes, ni adjetivos innecesarios, ni marketing.
        2. El 'Resumen' debe describir el impacto en ventas (ej: Venta de alta rotación, Ingreso significativo, etc).
        3. La 'Categoría' debe ser el sector técnico del producto.
        4. La 'Acción Sugerida' debe ser una tarea operativa (ej: Revisar stock, Sugerir combo, Verificar margen).
        5. Prohibido usar asteriscos (**) o Markdown.
        """
        
      
        response = model.generate_content(prompt)
        
        if response and response.text:
           
            texto_procesado = response.text.replace("*", "").replace("\n", "").strip()
          
            partes = [p.strip() for p in texto_procesado.split('|')]
            
            
            if len(partes) >= 3:
                return partes
            
           
            return [texto_procesado[:40], "General", "Sugerir producto complementario"]

    except Exception as e:
       
        print(f"⚠️ Error en AI_Service: {e}")
    
    
    return [
        f"¡Lleva tu {producto} ahora!", 
        "Venta", 
        "Sonreír al cliente y ofrecer un descuento en la próxima compra."
    ]