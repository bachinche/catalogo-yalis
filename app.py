import streamlit as st
from PIL import Image
import os

# ---------------- CONFIGURACIÓN GENERAL ----------------
st.set_page_config(
    page_title="Yalis | Catálogo",
    layout="wide"
)

# ---------------- ESTILOS (CSS) ----------------
st.markdown("""
<style>
body {
    background-color: #f5f6f7;
}
h1, h2, h3 {
    color: #1f2a37;
}
.boton {
    background-color: #111827;
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 20px;
    font-weight: 600;
}
.boton:hover {
    background-color: #1f2a37;
}
</style>
""", unsafe_allow_html=True)

# ---------------- ESTADO DE PÁGINA ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- FUNCIONES ----------------
def mostrar_galeria(titulo, carpeta):
    st.header(titulo)

    if not os.path.exists(carpeta):
        st.warning("No hay imágenes disponibles.")
        return

    imagenes = os.listdir(carpeta)
    cols = st.columns(3)

    for i, img in enumerate(imagenes):
        ruta = os.path.join(carpeta, img)
        imagen = Image.open(ruta)
        cols[i % 3].image(imagen, use_container_width=True)

    st.button("⬅ Volver al inicio", on_click=lambda: cambiar_pagina("home"))

def cambiar_pagina(pagina):
    st.session_state.page = pagina

# ---------------- HOME ----------------
if st.session_state.page == "home":
    st.title("YALIS")
    st.subheader("Mueblería · Closets · Baños")
    st.markdown("**Trabajos realizados a medida**")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🪑 MUEBLES"):
            cambiar_pagina("muebles")

    with col2:
        if st.button("🚪 CLOSETS"):
            cambiar_pagina("closets")

    with col3:
        if st.button("🚿 BAÑOS"):
            cambiar_pagina("banos")

    st.divider()

    st.markdown(
        "📲 **Solicite una cotización por WhatsApp**  \n"
        "[👉 Contactar](https://wa.me/51999999999)"
    )

# ---------------- GALERÍAS ----------------
elif st.session_state.page == "muebles":
    mostrar_galeria("Muebles", "images/muebles")

elif st.session_state.page == "closets":
    mostrar_galeria("Closets", "images/closets")

elif st.session_state.page == "banos":
    mostrar_galeria("Baños", "images/banos")
