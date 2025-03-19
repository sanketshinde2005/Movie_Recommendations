import streamlit as st
import requests
import time
import pandas as pd
import pickle
from huggingface_hub import hf_hub_download

st.set_page_config(page_title="Movie Recommender", layout="wide")  # Better layout


@st.cache_data
def fetch_poster(movie_id):
    """Fetch movie poster URL from TMDb API with retry logic."""
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d38f385f9e591a6bf106f8fb7f63548f&language=en-US'
    retries = 3  # Number of retries
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)  # 5-second timeout
            response.raise_for_status()  # Raise an error for 4xx and 5xx status codes
            data = response.json()
            if 'poster_path' in data and data['poster_path']:
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        except requests.exceptions.ConnectionError:
            time.sleep(2)  # Wait before retrying
        except requests.exceptions.RequestException:
            break  # Stop retrying on fatal errors
    return "https://via.placeholder.com/500x750?text=No+Image+Available"  # Fallback image


def recommend(movie):
    """Recommend movies based on similarity scores."""
    if movie not in movies['title'].values:
        return [], []  # Handle missing movies

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    # Efficiently get top 5 recommendations
    movies_list = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    recommended_movies_posters = [fetch_poster(movies.iloc[i[0]].movie_id) for i in movies_list]

    return recommended_movies, recommended_movies_posters


repo_id = "Sankeyyyyy/Movie-recommendation-system"


@st.cache_data
def load_data():
    """Load movie data and similarity matrix from Hugging Face."""
    movies_path = hf_hub_download(repo_id=repo_id, filename="movie_dict.pkl")
    similarity_path = hf_hub_download(repo_id=repo_id, filename="similarity.pkl")

    with open(movies_path, 'rb') as f:
        movies_dict = pickle.load(f)

    with open(similarity_path, 'rb') as f:
        similarity_matrix = pickle.load(f)

    return pd.DataFrame(movies_dict), similarity_matrix


movies, similarity = load_data()

st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    if names:
        columns = st.columns(5)
        for i in range(5):
            with columns[i]:
                st.text(names[i])
                st.image(posters[i])
    else:
        st.error("No recommendations found. Try another movie!")
