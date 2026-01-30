import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

import streamlit as st
from src.generator import StoryGenerator
from src.utils import create_download_link

# Page Configuration
st.set_page_config(page_title="AI Story Generator", page_icon="📖")

st.title("📖 AI Story Generator")
st.markdown("Transform your ideas into captivating stories using AI.")

# Sidebar Configuration
st.sidebar.header("Story Settings")
genre = st.sidebar.selectbox("Genre", ["Fantasy", "Sci-Fi", "Mystery", "Horror", "Romance", "Historical"])
tone = st.sidebar.selectbox("Tone", ["Serious", "Humorous", "Dark", "Inspirational", "Mysterious"])
length = st.sidebar.select_slider("Approximate Length", options=["Short", "Medium", "Long"])

# User Input
prompt = st.text_area("What is your story about?", placeholder="e.g., A detective finds a watch that can stop time...")

# State Management
if 'generated_story' not in st.session_state:
    st.session_state.generated_story = ""

if st.button("Generate Story"):
    if not prompt.strip():
        st.warning("Please enter a prompt first!")
    else:
        with st.spinner("Writing your story..."):
            generator = StoryGenerator()
            story = generator.generate_story(prompt, genre, length, tone)
            st.session_state.generated_story = story

# Display Result
if st.session_state.generated_story:
    st.markdown("---")
    st.markdown(st.session_state.generated_story)
    
    # Download Button
    st.download_button(
        label="Download Story as .txt",
        data=st.session_state.generated_story,
        file_name="generated_story.txt",
        mime="text/plain"
    )