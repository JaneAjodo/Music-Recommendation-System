import pickle
import streamlit as st
import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials

# -------------------------------
# 🔐 Spotify API Credentials
# -------------------------------
CLIENT_ID = "1897d46d6f4e4485bda3efaa490b0beb"
CLIENT_SECRET = "02aa8841adcf4815a0e9e746769d2fb4"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=15)

# -------------------------------
# 🔎 Helper Functions
# -------------------------------
def get_song_album_cover_url(song_name, artist_name):
    try:
        search_query = f"track:{song_name} artist:{artist_name}"
        results = sp.search(q=search_query, type="track")

        if results and results["tracks"]["items"]:
            return results["tracks"]["items"][0]["album"]["images"][0]["url"]
    except requests.exceptions.RequestException:
        st.warning(f"⚠️ Timeout while fetching album for: {song_name} by {artist_name}")
    return "https://i.postimg.cc/0QNxYz4V/social.png"  # Fallback image

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_names = []
    recommended_images = []

    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        title = music.iloc[i[0]].song
        image = get_song_album_cover_url(title, artist)

        recommended_names.append(title)
        recommended_images.append(image)

    return recommended_names, recommended_images

# -------------------------------
# 🎧 Streamlit UI
# -------------------------------
st.set_page_config(page_title="Music Recommender", layout="wide")
st.markdown("<h1 style='text-align: center;'>🎶 Music Recommendation System 🎶</h1>", unsafe_allow_html=True)

# Load Data
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Song selector
selected_song = st.selectbox("🎵 Choose a song you like:", music['song'].values)

# Show recommendations
if st.button('🎤 Recommend Songs'):
    names, posters = recommend(selected_song)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx], use_container_width=True)
            st.markdown(f"<p style='text-align: center;'>{names[idx]}</p>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>Made with ❤️ by Jane Ajodo</p>", unsafe_allow_html=True)
