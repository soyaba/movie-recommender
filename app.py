import streamlit as st
from src.load_data import cargar_datos
from src.recommender import crear_matriz, recomendar

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎬 Recomendador de Películas")
st.write("Introduce una película y te recomendamos 5 similares.")

# Cargar datos (solo una vez)
@st.cache_data
def cargar():
    df = cargar_datos()
    matriz = crear_matriz(df)
    return matriz

matriz = cargar()

# Lista de películas disponibles
peliculas = sorted(matriz.index.tolist())

# Input del usuario
pelicula = st.selectbox("🎥 Elige una película:", peliculas)

# Botón
if st.button("Recomendar"):
    resultados = recomendar(pelicula, matriz)
    st.subheader("🍿 Te recomendamos:")
    for i, r in enumerate(resultados, 1):
        st.write(f"{i}. {r}")
