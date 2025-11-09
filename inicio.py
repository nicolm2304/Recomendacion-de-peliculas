import pandas as pd 
ratings = pd.read_csv('ratings.csv')
ratings = pd.read_csv('ratings.csv')

rating_stats = ratings.groupby('movieId').agg({'rating': ['mean', 'count']})
rating_stats.columns = ['vote_average', 'vote_count']
rating_stats = rating_stats.reset_index()

metadata = movies.merge(rating_stats, on='movieId', how='inner')
metadata['vote_average'] = pd.to_numeric(metadata['vote_average'], errors='coerce')
metadata['vote_count'] = pd.to_numeric(metadata['vote_count'], errors='coerce')
metadata = metadata.dropna(subset=['vote_average', 'vote_count'])

C = metadata['vote_average'].mean()
m = metadata['vote_count'].quantile(0.90)

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v / (v + m) * R) + (m / (m + v) * C)

q_movies = metadata.loc[metadata['vote_count'] >= m].copy()
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)

print("=== Mejores películas según puntuación ponderada ===\n")
print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(15))

def mejores_por_genero(genero, n=10):
    if 'genres' not in metadata.columns:
        print("Error: la columna 'genres' no se encontró en movies.csv")
        return

    genero_movies = metadata[metadata['genres'].str.contains(genero, case=False, na=False)]
    if genero_movies.empty:
        print(f"No se encontraron películas del género '{genero}'.")
        return

    genero_movies = genero_movies.copy()
    genero_movies['score'] = genero_movies.apply(weighted_rating, axis=1)
    genero_movies = genero_movies.sort_values('score', ascending=False)

    print(f"\n=== Mejores películas del género: {genero} ===\n")
    print(genero_movies[['title', 'genres', 'vote_count', 'vote_average', 'score']].head(n))

while True:
    genero = input("\nIngrese un género para ver las mejores películas (o 'salir' para terminar): ").strip()
    if genero.lower() == 'salir':
        print("Saliendo del recomendador...")
        break
    mejores_por_genero(genero)
