codigo que recomienda peliculas
#este es un archivo de python
#keywords.csv, credits.csv,links.csv, links_small.csv, ratings_small.csv,movies_metadata.csv
# los de ariva son archivos de conjunto de datos de peliculas para las peliculas
import pandas as pd # Import Pandas

metadata = pd.read_csv('movies_metadata.csv', low_memory=False) # Load Movies Metadata

metadata.head(3) # Print the first three rows

# Calcular el porcentaje de votacion
C = metadata['vote_average'].mean()
print(C)

# Calcular el minimo de votos necesarios para crear la tabla, m
m = metadata['vote_count'].quantile(0.90)
print(m)

# se filtran todas las peliculas calificadas a una nueva lista/matriz
q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
q_movies.shape
