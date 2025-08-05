# 🎵 Music Recommendation System with Spotify API & Streamlit

This project recommends songs based on lyrical similarity using NLP techniques and displays them in a Streamlit app with album art from Spotify.

## 🔍 Features

- TF-IDF vectorization of song lyrics
- Cosine similarity-based recommendations
- Integration with Spotify Web API for album covers
- Streamlit app for user interaction

## 📁 Dataset

- [Spotify Million Song Dataset on Kaggle](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)
- Used 5,000-song sample for lightweight demo

## 🛠️ Tech Stack

- Python, Pandas, Scikit-learn, NLTK, Spotipy
- Streamlit for the web app

## 🚀 How to Run

1. Clone the repo  
2. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
3. Add your Spotify API credentials in `app.py`
4. Run the app:
    ```bash
    streamlit run app.py
    ```

## 📚 Learn More

- [Full Medium Article](https://medium.com/@janeajodo/building-a-music-recommendation-system-using-lyrics-and-streamlit-69adad17ce74) 
  

Built by **Jane Ajodo**  
Inspired by real-world streaming app recommendation engines.
