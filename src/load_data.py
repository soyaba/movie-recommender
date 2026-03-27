import pandas as pd

def cargar_datos():
    # Cargar ratings (usuario, película, puntuación)
    ratings = pd.read_csv(
        'data/ratings.csv',
        sep='\t',
        names=['user_id', 'movie_id', 'rating', 'timestamp']
    )

    # Cargar películas (id, título)
    movies = pd.read_csv(
        'data/movies.csv',
        sep='|',
        encoding='latin-1',
        usecols=[0, 1],
        names=['movie_id', 'title']
    )

    # Unir ambos por movie_id
    df = pd.merge(ratings, movies, on='movie_id')

    return df
