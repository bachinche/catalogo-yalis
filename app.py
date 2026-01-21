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
if st.session_state.page == "home":
    st.title("YALIS")
    st.subheader("Mueblería · Closets · Baños")
    st.markdown("**Trabajos realizados a medida**")
    st.divider()

    # ---------- FILAS ----------
    # Lista de cards: título, nombre de página, imagen
    cards = [
        {"titulo": "BAÑOS", "pagina": "bano", "img": "https://github.com/bachinche/catalogo-yalis/blob/main/images/bano/b1.jpeg"},
        {"titulo": "Centro de entretenimiento", "pagina": "centro", "img": "https://images.unsplash.com/photo-1598300052270-2be4d3e8dcff"},
        {"titulo": "Clósets", "pagina": "closets", "img": "https://images.unsplash.com/photo-1616628185561-f3d87c3d1cd2"},
        {"titulo": "Cocina", "pagina": "cocina", "img": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092"},
        {"titulo": "Dormitorio", "pagina": "dormitorio", "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c"},
        {"titulo": "Estantes", "pagina": "estantes", "img": "https://images.unsplash.com/photo-1586201375761-83865001b7d9"},
        {"titulo": "Porta copas", "pagina": "portacopas", "img": "https://images.unsplash.com/photo-1616628185599-b0f9812b2d3c"},
        {"titulo": "Escritorio/Librero", "pagina": "escritorio", "img": "https://images.unsplash.com/photo-1580894732444-42004a8dca12"},
        {"titulo": "Otros", "pagina": "otros", "img": "https://images.unsplash.com/photo-1581091215361-6e69e0b71f55"},
    ]

    # Recorremos las cards de 3 en 3 para crear filas
    for i in range(0, len(cards), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(cards):
                card = cards[i + j]
                with col:
                    # Botón invisible para cambiar de página
                    if st.button(" ", key=f"card_{card['pagina']}"):
                        cambiar_pagina(card["pagina"])

                    # Card HTML
                    st.markdown(f"""
                    <div class="card">
                        <img src="{card['img']}">
                        <div class="card-title">{card['titulo']}</div>
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







