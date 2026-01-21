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

    # ---------- FILA 0 ----------
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🚿 Baños"):
            cambiar_pagina("bano")

    with col2:
        if st.button("📺 Centro de entretenimiento"):
            cambiar_pagina("centro")

    with col3:
        if st.button("🚪 Clósets"):
            cambiar_pagina("closets")

    # ---------- FILA 1 ----------
    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("🍽️ Cocina"):
            cambiar_pagina("cocina")

    with col5:
        if st.button("🛏️ Dormitorio"):
            cambiar_pagina("dormitorio")

    with col6:
        if st.button("📚 Estantes"):
            cambiar_pagina("estantes")

    # ---------- FILA 2 ----------
    col7, col8, col9 = st.columns(3)

    with col7:
        if st.button("🍷 Porta copas"):
            cambiar_pagina("portacopas")

    with col8:
        if st.button("🚪 Escritorio/Librero"):
            cambiar_pagina("escritorio")

    with col9:
        if st.button("📦 Otros"):
            cambiar_pagina("otros")

    st.divider()

    st.markdown(
        "📲 **Solicite una cotización por WhatsApp**  \n"
        "[👉 Contactar](https://wa.me/51999999999)"
    )


# ---------------- GALERÍAS ----------------
elif st.session_state.page == "closets":
    mostrar_galeria("Clóset", "images/closet")

elif st.session_state.page == "bano":
    mostrar_galeria("Baños", "images/bano")

elif st.session_state.page == "centro":
    mostrar_galeria("Centro de entretenimiento", "images/centro")

elif st.session_state.page == "cocina":
    mostrar_galeria("Cocina", "images/cocina")

elif st.session_state.page == "dormitorio":
    mostrar_galeria("Dormitorio", "images/dormitorio")

elif st.session_state.page == "estantes":
    mostrar_galeria("Estantes", "images/estantes")

elif st.session_state.page == "portacopas":
    mostrar_galeria("Porta copas", "images/portacopas")

elif st.session_state.page == "escritorio":
    mostrar_galeria("Puerta falsa", "images/puertafalsa")

elif st.session_state.page == "otros":
    mostrar_galeria("Otros", "images/otros")

