import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def crear_matriz(df):
    # Matriz: filas = películas, columnas = usuarios
    matriz = df.pivot_table(
        index='title',
        columns='user_id',
        values='rating'
    ).fillna(0)

    return matriz

def recomendar(pelicula, matriz, n=5):
    # Calcular similitud entre todas las películas
    similitud = cosine_similarity(matriz)
    sim_df = pd.DataFrame(similitud, index=matriz.index, columns=matriz.index)

    # Obtener las n películas más similares
    similares = sim_df[pelicula].sort_values(ascending=False)[1:n+1]

    return similares.index.tolist()
