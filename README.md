# 📌 Registro Básico de Ventas Diarias

## 📖 Descripción
Sistema básico para el registro y validación de ventas diarias.  
Permite calcular el subtotal, aplicar descuento VIP del 10% y mostrar el total final de forma clara y legible.


---

## 🎯 Objetivo
Desarrollar una aplicación sencilla que permita:

- Registrar ventas correctamente.
- Calcular el subtotal (precio × cantidad).
- Aplicar descuento VIP del 10%.
- Calcular el total final.
- Mostrar un resumen claro de la venta.

---

## 📐 Reglas de Negocio

- **Subtotal = precio × cantidad**
- **Descuento VIP = 10% del subtotal**
- **Total Final = subtotal − descuento (si aplica)**

---

## ⚙️ Funcionalidades Implementadas

- Registro de producto
- Ingreso de cantidad y precio unitario
- Validación de datos
- Cálculo automático de subtotal
- Aplicación de descuento VIP
- Cálculo del total final
- Visualización clara del resumen de venta

---

## 🌿 Estrategia de Ramas (Git Flow Simplificado)

- `main` → versión estable  
- `develop` → integración de funcionalidades  
- `feature/*` → desarrollo de nuevas funcionalidades  
- `test/*` → prueba del programa

---

## 🧪 Ejecutar pruebas

Desde la raíz del proyecto ejecutar:

```bash
python3 -m unittest discover
```

Para ejecutar un archivo específico:

```bash
python3 -m unittest tests/test_validacion.py
```

---

## ✔️ Estado del proyecto

- Tests implementados
- Arquitectura por features
- Separación de responsabilidades
- Buenas prácticas aplicadas

---


## 🛠 Tecnologías
  
- Python  
- Git  
- GitHub  

---
## Requerimientos

- Tener instaladom python 3 para la ejecucion optima del programa.

---

## AUTHOR

- Carlos Daniel Molina Ordoñez.
