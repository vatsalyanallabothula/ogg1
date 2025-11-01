import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Telugu Movie Jukebox", page_icon="🎵", layout="centered")
st.markdown("<h1 style='text-align: center; color: red;'>🎬 Telugu Movie Jukebox 🎧</h1>", unsafe_allow_html=True)

movie_choice = st.sidebar.selectbox(
    "🎥 Choose a Movie Jukebox",
    ("Select...", "They Call Him OG", "Badhri", "Kushi")
)

# -------------------------------
# 🎵 FUNCTION TO DISPLAY JUKEBOX
# -------------------------------
def display_jukebox(movie_name, poster_path, songs):
    st.markdown(f"<h2 style='text-align: center; color: orange;'>{movie_name} 🎧</h2>", unsafe_allow_html=True)
    
    # Poster
    if Path(poster_path).exists():
        st.image(str(poster_path), use_container_width=True)
    else:
        st.warning(f"⚠️ Poster not found for {movie_name}!")

    # Songs
    if not songs:
        st.warning(f"⚠️ No songs found for {movie_name}!")
        return

    st.markdown("---")
    for song_path in songs:
        path = Path(song_path)
        if path.exists():
            st.subheader(f"🎵 {path.stem}")
            with open(path, "rb") as f:
                audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/mp3")
                st.download_button(
                    label="⬇️ Download Song",
                    data=audio_bytes,
                    file_name=path.name,
                    mime="audio/mp3"
                )
            st.markdown("---")
        else:
            st.warning(f"⚠️ File not found: {song_path}")

# -------------------------------
# 🎶 SONG PATHS
# -------------------------------

# OG MOVIE SONGS
og_poster = r"C:\Users\vs\Videos\they-call-him-og-2025-X2HpTQ.jpg"
og_songs = [
    r"C:\Users\vs\Downloads\Hungry Cheetah.mp3",
    r"C:\Users\vs\Downloads\Washi O Washi.mp3",
    r"C:\Users\vs\Downloads\Suvvi Suvvi.mp3",
    r"C:\Users\vs\Downloads\Trance of OMI.mp3",
    r"C:\Users\vs\Downloads\Guns And Roses.mp3",
    r"C:\Users\vs\Downloads\Kiss Kiss Bang Bang.mp3"
]

# BADHRI MOVIE SONGS
badhri_poster = r"C:\Users\vs\Videos\badhri.jpg"
badhri_songs = [
    r"C:\Users\vs\Downloads\Yey Chikitha-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Vevela Mainala-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Bangala Kathamlo-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Am Indian-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Chali pidugullo-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Varamanti Manase-SenSongsMp3.Co.mp3"
]

# KUSHI MOVIE SONGS
kushi_poster = r"C:\Users\vs\Videos\kushi.jpeg"
kushi_songs = [
    r"C:\Users\vs\Downloads\Ammaye Sannaga-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Cheliya Cheliya-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Aaduvari Matalaku-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Holi Holi-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Premante-SenSongsMp3.Co.mp3",
    r"C:\Users\vs\Downloads\Ye Mera Jahan-SenSongsMp3.Co.mp3"
]

# -------------------------------
# 🎬 DISPLAY SELECTED MOVIE
# -------------------------------
if movie_choice == "They Call Him OG":
    display_jukebox("They Call Him OG", og_poster, og_songs)

elif movie_choice == "Badhri":
    display_jukebox("Badhri", badhri_poster, badhri_songs)

elif movie_choice == "Kushi":
    display_jukebox("Kushi", kushi_poster, kushi_songs)

else:
    st.info("👈 Choose a movie from the sidebar to view its jukebox.")
