codigo que recomienda peliculas
#este es un archivo de python
#keywords.csv, credits.csv,links.csv, links_small.csv, ratings_small.csv,movies_metadata.csv
# los de ariva son archivos de conjunto de datos de peliculas para las peliculas
# Se importa Pandas
import pandas as pd 
# Se cargan las peliculas de metadata
metadata = pd.read_csv('movies_metadata.csv', low_memory=False)
# Imprimir las tres primeras lineas
metadata.head(3)

# Funcion que computa y pesa el puntaje de cada pelicula
def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

# Calcular el porcentaje de votacion
C = metadata['vote_average'].mean()
print(C)

# Calcular el minimo de votos necesarios para crear la tabla, m
m = metadata['vote_count'].quantile(0.90)
print(m)

# se filtran todas las peliculas calificadas a una nueva lista/matriz
q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
q_movies.shape

metadata.shape

# Definir la nueva categoria 'score' y calcular su valor con la funcion `weighted_rating()`
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

#sortear las peliculas basadas en los resultados anteriores
q_movies = q_movies.sort_values('score', ascending=False)

#se imprimen las mejores 15 peliculas
q_movies[['title', 'vote_count', 'vote_average', 'score']].head(20)
