import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    try :
         response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=f4024b4646362fa33d687015a7e8de3b&language=en-US".format(movie_id),timeout=10)
         response.raise_for_status()
         data = response.json()
         return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:4]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movie_dict= pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movie_dict)
st.title('Movie Recommender System')


selected_movie_name= st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values)
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)


    col1, col2, col3 = st.columns(3)

    with col1:
        st.header(names[0])
        st.image(posters[0])

    with col2:
        st.header(names[1])
        st.image(posters[1])

    with col3:
        st.header(names[2])
        st.image(posters[2])