import streamlit as st
import pandas as pd
from utils import capture_image_from_webcam, detect_emotion

st.set_page_config(page_title="Emotion-based Music Recommender 🎵", layout="centered")

st.title("🎧 Emotion-Based Music Recommender")
st.write("This app captures your facial emotion and recommends songs that match your mood!")

if st.button("📸 Capture Emotion"):
    st.info("Opening webcam. Press SPACE to capture your image...")
    image_path = capture_image_from_webcam()

    if image_path:
        st.success("✅ Image captured successfully!")
        st.image(image_path, caption="Captured Image", width=300)

        st.info("🔍 Detecting emotion...")
        try:
            emotion = detect_emotion(image_path)
            st.success(f"🧠 Detected Emotion: **{emotion.capitalize()}**")

            # Load songs
            df = pd.read_csv("song.csv")
            recommendations = df[df['emotion'].str.lower() == emotion.lower()]

            if not recommendations.empty:
                st.subheader("🎵 Recommended Songs for You:")
                for _, row in recommendations.iterrows():
                    st.markdown(f"- **{row['song_name']}** by *{row['artist']}*")
            else:
                st.warning("😔 No songs found for this emotion.")
        except Exception as e:
            st.error(f"❌ Error detecting emotion: {e}")
    else:
        st.error("❌ Failed to capture image.")
