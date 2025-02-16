import streamlit as st
import requests
import time
import pandas as pd
import pickle
from huggingface_hub import hf_hub_download

# Function to fetch movie poster from TMDb API
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d38f385f9e591a6bf106f8fb7f63548f&language=en-US'
    retries = 3  # Number of retries
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)  # 5-second timeout
            response.raise_for_status()  # Raise an error for 4xx and 5xx status codes
            data = response.json()
            if 'poster_path' in data and data['poster_path']:
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
            else:
                return "https://via.placeholder.com/500x750?text=No+Image+Available"
        except requests.exceptions.ConnectionError:
            print(f"Connection error. Retrying {attempt + 1}/{retries}...")
            time.sleep(2)  # Wait before retrying
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
            break  # Don't retry for HTTP errors like 404
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            break  # Stop retrying if it's another error
    return "https://via.placeholder.com/500x750?text=No+Image+Available"  # Default fallback

# Function to recommend similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Fetching movie ID
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))  # Fetch poster

    return recommended_movies, recommended_movies_posters

# Download movie data and similarity matrix from Hugging Face
repo_id = "https://huggingface.co/Sankeyyyyy/Movie-recommendation-system/tree/main"

movies_path = hf_hub_download(repo_id=repo_id, filename="movie_dict.pkl")
similarity_path = hf_hub_download(repo_id=repo_id, filename="similarity.pkl")

# Load movie data and similarity matrix
with open(movies_path, 'rb') as f:
    movies_dict = pickle.load(f)

with open(similarity_path, 'rb') as f:
    similarity = pickle.load(f)

movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    columns = st.columns(5)
    for i in range(5):
        with columns[i]:
            st.text(names[i])
            st.image(posters[i])
