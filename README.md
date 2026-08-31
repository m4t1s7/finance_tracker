# 💸 Finance Tracker (Streamlit)

Aplicación web interactiva desarrollada con **Streamlit** para la captura, validación y estructuración de transacciones financieras en formato **JSON**.

---

## 🚀 Cómo ejecutar la aplicación

1. Abre tu terminal o consola (PowerShell o CMD).
2. Ve al directorio del proyecto:
   ```bash
   cd C:\Users\USUARIO\Desktop\tracker
   ```
3. Ejecuta Streamlit:
   ```bash
   python -m streamlit run app.py
   ```
4. Se abrirá automáticamente en tu navegador predeterminado (usualmente en `http://localhost:8501`).

---

## 📋 Estructura de Campos

| Campo | Componente Streamlit | Formato / Opciones |
|---|---|---|
| **Fecha** | `st.date_input` | Estructura Mes/Día/Año (`MM/DD/YYYY`) |
| **Descripción** | `st.text_input` | Texto libre |
| **Categoría** | `st.selectbox` | `Ingresos`, `Transporte`, `Comida`, `Suscripciones`, `Inversiones` |
| **Tipo** | `st.radio` | `Ingreso`, `Egreso` |
| **Monto** | `st.number_input` | Número entero (`format="%d"`) |

---

## 📦 Salida JSON Generada

Cada envío genera y captura un diccionario estructurado como este:

```json
{
    "Fecha": "08/30/2026",
    "Descripcion": "Almuerzo de negocios",
    "Categoria": "Comida",
    "Tipo": "Egreso",
    "Monto": 45000
}
```
