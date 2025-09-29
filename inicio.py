codigo que recomienda peliculas
#este es un archivo de python
#keywords.csv, credits.csv,links.csv, links_small.csv, ratings_small.csv,movies_metadata.csv
# los de ariva son archivos de conjunto de datos de peliculas para las peliculas
import pandas as pd # Import Pandas

metadata = pd.read_csv('movies_metadata.csv', low_memory=False) # Load Movies Metadata

metadata.head(3) # Print the first three rows
