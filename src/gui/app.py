import customtkinter as ctk
from tkinter import messagebox
import threading 
from src.features.validacion.validacion import calcular_subtotal, calcular_descuento_vip, calcular_total_final
from src.services.almacenamiento import guardar_venta_mysql, obtener_ventas
from src.services.ai_service import obtener_analisis_ia
from src.models.ventas import Venta
from src.utils.formato import formatear_moneda

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppVentas(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sales Intelligence Pro - Colombia")
        self.geometry("900x750")

        self.tabview = ctk.CTkTabview(self, width=850, height=680)
        self.tabview.pack(padx=20, pady=20)

        self.tab_registro = self.tabview.add("🛒 Registro de Ventas")
        self.tab_historial = self.tabview.add("📜 Historial de Ventas")

        self.setup_tab_registro()
        self.setup_tab_historial()

    def setup_tab_registro(self):
        self.lbl_titulo = ctk.CTkLabel(self.tab_registro, text="NUEVA VENTA", font=ctk.CTkFont(size=20, weight="bold"))
        self.lbl_titulo.pack(pady=15)

        self.frame_form = ctk.CTkFrame(self.tab_registro)
        self.frame_form.pack(pady=10, padx=60, fill="x")

        self.ent_prod = ctk.CTkEntry(self.frame_form, placeholder_text="Nombre del Producto", height=40)
        self.ent_prod.pack(pady=10, padx=20, fill="x")

        self.ent_cant = ctk.CTkEntry(self.frame_form, placeholder_text="Cantidad", height=40)
        self.ent_cant.pack(pady=10, padx=20, fill="x")

        self.ent_prec = ctk.CTkEntry(self.frame_form, placeholder_text="Precio Unitario (COP)", height=40)
        self.ent_prec.pack(pady=10, padx=20, fill="x")

        self.var_vip = ctk.BooleanVar()
        self.check_vip = ctk.CTkCheckBox(self.frame_form, text="Cliente VIP", variable=self.var_vip)
        self.check_vip.pack(pady=10)

       
        self.btn_reg = ctk.CTkButton(self.tab_registro, text="PROCESAR VENTA CON IA", 
                                     font=ctk.CTkFont(weight="bold"),
                                     fg_color="#2ecc71", hover_color="#27ae60",
                                     height=50, command=self.iniciar_proceso_venta)
        self.btn_reg.pack(pady=20)

        self.txt_ia = ctk.CTkTextbox(self.tab_registro, height=180, width=550, font=("Consolas", 12))
        self.txt_ia.pack(pady=10)
        self.txt_ia.insert("0.0", "🤖 Listo para analizar...")

    def setup_tab_historial(self):
        import tkinter as tk
        from tkinter import ttk

        self.btn_refrescar = ctk.CTkButton(self.tab_historial, text="🔄 Actualizar Historial", command=self.cargar_datos_tabla)
        self.btn_refrescar.pack(pady=15)

        self.tabla = ttk.Treeview(self.tab_historial, columns=("P", "C", "T", "Cat"), show="headings", height=15)
        self.tabla.heading("P", text="Producto")
        self.tabla.heading("C", text="Cant")
        self.tabla.heading("T", text="Total (COP)")
        self.tabla.heading("Cat", text="Categoría")
        self.tabla.pack(expand=True, fill="both", padx=20, pady=20)
        self.cargar_datos_tabla()

    def iniciar_proceso_venta(self):
        
        self.btn_reg.configure(state="disabled", text="⏳ PROCESANDO CON IA...", fg_color="#f1c40f")
        self.txt_ia.delete("0.0", "end")
        self.txt_ia.insert("0.0", "🤖 Conectando con Gemini en la nube...")
        
        
        threading.Thread(target=self.procesar_venta_logica, daemon=True).start()

    def procesar_venta_logica(self):
        try:
            p = self.ent_prod.get()
            c = int(self.ent_cant.get())
            pr = float(self.ent_prec.get())
            v = self.var_vip.get()

       
            sub = calcular_subtotal(pr, c)
            desc = calcular_descuento_vip(sub, v)
            tot = calcular_total_final(sub, desc)
            
           
            ia = obtener_analisis_ia(p, pr, c, 0)
            
       
            venta_obj = Venta(p, c, pr, v, sub, desc, tot, ia[1], ia[0], ia[2])
            guardar_venta_mysql(venta_obj)

            
            self.after(0, lambda: self.finalizar_exito(tot, ia))

        except Exception as e:
            self.after(0, lambda: self.finalizar_error(e))

    def finalizar_exito(self, tot, ia):
        resumen = f"✅ VENTA COMPLETADA\n{'-'*40}\n💰 TOTAL: {formatear_moneda(tot)}\n🏷️ CAT: {ia[1]}\n✨ ESLOGAN: {ia[0]}\n💡 CONSEJO: {ia[2]}"
        self.txt_ia.delete("0.0", "end")
        self.txt_ia.insert("0.0", resumen)
        
        
        self.btn_reg.configure(state="normal", text="PROCESAR VENTA CON IA", fg_color="#2ecc71")
        
        
        self.ent_prod.delete(0, 'end')
        self.ent_cant.delete(0, 'end')
        self.ent_prec.delete(0, 'end')
        self.cargar_datos_tabla()
        messagebox.showinfo("Éxito", "Venta registrada.")

    def finalizar_error(self, e):
        self.btn_reg.configure(state="normal", text="PROCESAR VENTA CON IA", fg_color="#2ecc71")
        messagebox.showerror("Error", f"Verifique los datos o la conexión: {e}")

    def cargar_datos_tabla(self):
        for item in self.tabla.get_children(): self.tabla.delete(item)
        ventas = obtener_ventas()
        for v in ventas:
            self.tabla.insert("", "end", values=(v.producto, v.cantidad, formatear_moneda(v.total), v.categoria))

if __name__ == "__main__":
    app = AppVentas()
    app.mainloop()