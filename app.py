import streamlit as st
import pickle
import pandas as pd
import requests

# --- 1. Added Cache to Speed Up API Calls ---
@st.cache_data
def fetch_movie_info(movie_title):
    api_key = "1463b864"
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        poster = data.get('Poster', "https://via.placeholder.com/500x750?text=No+Poster")
        rating = data.get('imdbRating', "N/A")
        year = data.get('Year', "N/A")
        genre = data.get('Genre', "N/A")
        return poster, rating, year, genre
    except:
        return "https://via.placeholder.com/500x750", "N/A", "N/A", "N/A"

# --- 2. Added Cache to Speed Up File Loading ---
@st.cache_resource
def load_data():
    try:
        # PATH UPDATED TO YOUR FOLDER STRUCTURE
        movies_dict = pickle.load(open('models/movie_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)
        similarity = pickle.load(open('models/similarity.pkl', 'rb'))
        return movies, similarity
    except Exception as e:
        st.error("Error: Pickle files not found in 'models/' folder!")
        return None, None

movies, similarity = load_data()

# --- UI Configuration (NO CHANGES HERE) ---
st.set_page_config(page_title="CineMatch AI", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stButton>button {
        background-color: #e50914;
        color: white;
        border-radius: 10px;
        width: 100%;
        font-weight: bold;
        border: none;
        height: 3em;
    }
    .stButton>button:hover { background-color: #ff0a16; color: white; }
    h1 { color: #e50914; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar (NO CHANGES HERE) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2503/2503508.png", width=80)
st.sidebar.title("CineMatch AI")
st.sidebar.markdown("---")
st.sidebar.info("Content-based recommendation engine using Machine Learning.")

# --- Header ---
st.markdown("<h1 style='text-align: center;'>🎬 CINEMATCH</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Your Personal Movie Recommender System</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Recommendation Logic ---
if movies is not None:
    selected_movie_name = st.selectbox('Search for a movie you like...', movies['title'].values)

    if st.button('Get Recommendations'):
        # Added a spinner so user knows it's working
        with st.spinner('Fetching the best movies for you...'):
            movie_index = movies[movies['title'] == selected_movie_name].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

            st.success(f"Top 10 Recommendations for '{selected_movie_name}':")

            # --- Row 1 ---
            st.subheader("🌟 Top Picks")
            cols1 = st.columns(5)
            for i in range(5):
                with cols1[i]:
                    title = movies.iloc[movies_list[i][0]].title
                    poster, rating, year, genre = fetch_movie_info(title)
                    st.image(poster)
                    st.markdown(f"**{title}**")
                    st.caption(f"⭐ {rating} | 📅 {year}")

            st.markdown("---")

            # --- Row 2 ---
            st.subheader("🔍 You Might Also Like")
            cols2 = st.columns(5)
            for i in range(5, 10):
                with cols2[i-5]:
                    title = movies.iloc[movies_list[i][0]].title
                    poster, rating, year, genre = fetch_movie_info(title)
                    st.image(poster)
                    st.markdown(f"**{title}**")
                    st.caption(f"⭐ {rating} | 📅 {year}")

# --- Footer ---
st.markdown("<br><hr><center>Built with Machine Learning & Streamlit</center>", unsafe_allow_html=True)