from urllib import response

import streamlit as st
from datetime import datetime
import requests

mi_URL = "unaURLdeejemplo.com"

st.set_page_config(
    page_title="Tracker Financiero",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .tracker-card {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.75), rgba(15, 23, 42, 0.9));
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 32px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5), 0 0 25px rgba(99, 102, 241, 0.1);
        backdrop-filter: blur(16px);
        margin-bottom: 24px;
    }

    .gradient-title {
        background: linear-gradient(135deg, #818CF8 0%, #C084FC 50%, #F472B6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.2rem;
        margin-bottom: 6px;
        letter-spacing: -0.02em;
    }

    .subtitle {
        color: #94A3B8;
        font-size: 0.95rem;
        margin-bottom: 8px;
    }

    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(99, 102, 241, 0.15);
        color: #A5B4FC;
        border: 1px solid rgba(99, 102, 241, 0.3);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 600;
        margin-bottom: 14px;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 28px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        width: 100% !important;
        transition: all 0.25s ease-in-out !important;
        box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39) !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(99, 102, 241, 0.55) !important;
        background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%) !important;
    }

    div.stButton > button:active {
        transform: translateY(0px) !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tracker-card">
    <div class="status-badge">
        <span>✨</span> Formulario de Registro
    </div>
    <div class="gradient-title">Tracker</div>
    <div class="subtitle">Registra tus movimientos financieros.</div>
</div>
""", unsafe_allow_html=True)

with st.form("registro_formulario", clear_on_submit=False):
    st.markdown("#### 📝 Datos de la Transacción")

    col1, col2 = st.columns(2)

    with col1:
        fecha_seleccionada = st.date_input(
            label="📅 Fecha",
            value=datetime.today(),
            format="MM/DD/YYYY",
            help="Estructura seleccionada: Mes/Día/Año (MM/DD/YYYY)"
        )

    with col2:
        tipo_seleccionado = st.radio(
            label="🔄 Tipo de Movimiento",
            options=["Ingreso", "Egreso"],
            horizontal=True,
            help="Selecciona si es una entrada o salida de dinero"
        )

    descripcion_texto = st.text_input(
        label="📄 Descripción",
        placeholder="Ej: Pago de nómina, Cena con amigos, Suscripción a Spotify...",
        help="Detalla el motivo del movimiento"
    )

    col3, col4 = st.columns(2)

    with col3:
        categorias_disponibles = [
            "Ingresos",
            "Transporte",
            "Comida",
            "Suscripciones",
            "Inversiones"
        ]
        categoria_seleccionada = st.selectbox(
            label="🏷️ Categoría",
            options=categorias_disponibles,
            help="Clasificación del movimiento"
        )

    with col4:
        monto_valor = st.number_input(
            label="💰 Monto",
            min_value=0,
            step=1,
            format="%d",
            help="Valor monetario expresado como número entero"
        )

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
    
    enviado = st.form_submit_button("🚀 Registrar Transacción")

if enviado:
    if fecha_seleccionada and descripcion_texto and categoria_seleccionada and tipo_seleccionado and monto_valor:
        datos_json = {
            "Fecha": fecha_seleccionada.strftime("%m/%d/%Y"),
            "Descripcion": descripcion_texto.strip(),
            "Categoria": categoria_seleccionada,
            "Tipo": tipo_seleccionado,
            "Monto": int(monto_valor)
        }
        try:
            respuesta = requests.post(mi_URL, json=datos_json, timeout=10)
            if respuesta.status_code == 200:
                st.toast("¡Registro enviado con éxito a Excel!", icon="✅")
            else:
                st.toast(f"**Error**, tu registro no se ha podido guardar", icon="❌")
        except requests.exceptions.RequestException as e:
            st.toast("Error al enviar los datos. Por favor, inténtalo de nuevo.", icon="❌")
    else:
        st.toast("Por favor, completa todos los campos antes de enviar.", icon="⚠️")

