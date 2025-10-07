# Movie-Recommender-System
This project implements a content-based movie recommender system using metadata from the TMDB (The Movie Database) dataset. The system recommends movies based on similarity of tags generated from movie genres, keywords, cast, and crew information.

# Features
 - Data merging and cleaning of TMDB movies and credits datasets
 - Extraction and processing of relevant features:
     - Genres
     - keywords
     - cast(top 3 actor)
     - crew(director)
 - Text preprocessing including lowercasing, and stemming
 - Creation of combined tags from multiple metadata fields
 - Vectorization of text data using CountVectorizer
 - Similarity calculation between movies using cosine similarity
 - Movie recommendations based on closest matching tags

