import streamlit as st
from PIL import Image
import os

# Configuración de la página
st.set_page_config(
    page_title="Yalis | Catálogo",
    layout="wide"
)

st.title("YALIS")
st.subheader("Mueblería – Trabajos realizados")
st.markdown("Fabricación de **muebles**, **closets** y **baños** a medida.")

st.divider()

# Función para mostrar imágenes por categoría
def mostrar_categoria(nombre, carpeta):
    st.header(nombre)
    cols = st.columns(3)

    imagenes = os.listdir(carpeta)
    for i, img in enumerate(imagenes):
        ruta = os.path.join(carpeta, img)
        imagen = Image.open(ruta)
        cols[i % 3].image(imagen, use_container_width=True)

# Categorías
mostrar_categoria("🪑 Muebles", "images/muebles")
mostrar_categoria("🚪 Closets", "images/closets")
mostrar_categoria("🚿 Baños", "images/banos")

st.divider()

# Botón WhatsApp
st.markdown(
    """
    ### 📲 ¿Desea una cotización?
    [👉 Contáctenos por WhatsApp](https://wa.me/51999999999)
    """
)
