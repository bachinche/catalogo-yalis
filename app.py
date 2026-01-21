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
.card {
    border-radius: 16px;
    overflow: hidden;
    background: white;
    box-shadow: 0 6px 16px rgba(0,0,0,0.10);
    cursor: pointer;
    transition: all 0.25s ease;
    margin-bottom: 20px;
}

.card:hover {
    box-shadow: 0 14px 30px rgba(0,0,0,0.18);
    transform: translateY(-6px);
}

.card img {
    width: 100%;
    height: 230px;
    object-fit: cover;
    display: block;
}

.card-title {
    padding: 16px;
    font-size: 22px;
    font-weight: 700;
    text-align: center;
    color: #111827;
    letter-spacing: 0.5px;
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
# ---------------- HOME ----------------
if st.session_state.page == "home":
    st.title("YALIS")
    st.subheader("Mueblería · Closets · Baños")
    st.markdown("**Trabajos realizados a medida**")
    st.divider()

    # Lista de categorías con su página y URL de imagen
    categorias = [
        {"titulo": "BAÑOS", "pagina": "banos", "img": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a"},
        {"titulo": "CENTRO DE ENTRETENIMIENTO", "pagina": "centro", "img": "https://images.unsplash.com/photo-1581090700227-4f8777f4d4a5"},
        {"titulo": "CLÓSETS", "pagina": "closets", "img": "https://images.unsplash.com/photo-1580587771525-78b9dba3b914"},
        {"titulo": "COCINA", "pagina": "cocina", "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c"},
        {"titulo": "DORMITORIO", "pagina": "dormitorio", "img": "https://images.unsplash.com/photo-1598300054739-1c4c10f0c6a8"},
        {"titulo": "ESTANTES", "pagina": "estantes", "img": "https://images.unsplash.com/photo-1616627988427-5e1e6c5fa5c1"},
        {"titulo": "PORTA COPAS", "pagina": "portacopas", "img": "https://images.unsplash.com/photo-1616627992123-3f44c3b0d6e2"},
        {"titulo": "ESCRITORIO/LIBRERO", "pagina": "escritorio", "img": "https://images.unsplash.com/photo-1616627994521-9f5c3a0c9b2e"},
        {"titulo": "OTROS", "pagina": "otros", "img": "https://images.unsplash.com/photo-1616627996783-1a2c5c0e9c3d"},
    ]

    # Mostrar cards en filas de 3
    for i in range(0, len(categorias), 3):
        cols = st.columns(3)
        for j, categoria in enumerate(categorias[i:i+3]):
            with cols[j]:
                if st.button("", key=f"card_{categoria['pagina']}"):
                    cambiar_pagina(categoria["pagina"])
                st.markdown(f"""
                <div class="card">
                    <img src="{categoria['img']}">
                    <div class="card-title">{categoria['titulo']}</div>
                </div>
                """, unsafe_allow_html=True)

    st.divider()

    st.markdown(
        "📲 **Solicite una cotización por WhatsApp**  \n"
        "[👉 Contactar](https://wa.me/51999999999)"
    )

# ---------------- GALERÍAS ----------------
elif st.session_state.page == "closets":
    mostrar_galeria("Clóset", "images/closet")

elif st.session_state.page == "banos":
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

elif st.session_state.page == "puertafalsa":
    mostrar_galeria("Puerta falsa", "images/puertafalsa")

elif st.session_state.page == "otros":
    mostrar_galeria("Otros", "images/otros")
