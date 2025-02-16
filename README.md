# Movie Recommender System

## Overview
Movie Recommender System is a web application that suggests movies to users based on their preferences. It utilizes an AI/ML model trained on a dataset from TMDB (The Movie Database) and is deployed using Streamlit. The recommendation engine is built using vector transformation techniques and the model is stored as pickle files on Hugging Face for easy accessibility.

## Features
- **Personalized Recommendations**: Users can input a movie title, and the system suggests similar movies based on content similarity.
- **Real-Time Search**: The application instantly fetches recommendations when a user searches for a movie.
- **Interactive UI**: Built with Streamlit, the webpage provides a simple yet effective user interface.
- **Fast & Efficient**: Uses machine learning techniques to generate recommendations quickly.

## Technologies Used
- **Python**: Used for backend logic and ML model development.
- **Jupyter Notebook**: Model training and data preprocessing were performed in Jupyter Notebook.
- **Machine Learning**: 
  - Vector transformation techniques such as TF-IDF or Count Vectorizer for text-based movie similarity.
  - Cosine similarity or other distance metrics for recommendation generation.
- **TMDB Dataset**: Movie metadata, including genres, descriptions, and cast information, was used for training.
- **Pickle Files**: The trained model is stored as a pickle file and hosted on Hugging Face.
- **Streamlit**: Web framework used to deploy the model in an interactive and user-friendly manner.
- **Hugging Face**: Storage for model files and easy access for deployment.

## How It Works
1. **User Input:**
   - Users enter the name of a movie into the search bar.
   - The system processes the input and retrieves similar movies.

2. **Fetching Recommendations:**
   - The input movie title is transformed into vector form using the trained model.
   - Cosine similarity or other distance metrics are applied to find similar movies.

3. **Displaying Results:**
   - The recommended movies are displayed on the webpage with their titles, posters, and additional details fetched from the TMDB database.

## Setup and Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/sanketshinde2005/MovieRecommender
   ```
2. Navigate to the project directory:
   ```bash
   cd MovieRecommender
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Webpage Screenshots
![image](https://github.com/user-attachments/assets/a82362d3-767c-4827-9750-913c0d0fb088)
![image](https://github.com/user-attachments/assets/c62c6590-3ef1-4a30-852b-48fc157a448c)



## Future Enhancements
- **User-Based Collaborative Filtering**: Enhance recommendations by incorporating user ratings and preferences.
- **Genre-Based Filters**: Allow users to refine recommendations based on movie genres.
- **Movie Watchlist**: Enable users to save and manage a list of favorite movies.
- **Deployment on Cloud**: Host the system on cloud platforms like AWS/GCP for broader accessibility.

## My Work
[Movie Recommender Webpage](https://movierecommendations-rgq8fjvf4hp2jmwiwystfb.streamlit.app/)
