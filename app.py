import streamlit as st
from utils import toggle_webcam
from components import display_uploaded_images, display_summary

# Initialize session state for webcam
if 'webcam_enabled' not in st.session_state:
    st.session_state.webcam_enabled = False

# Create titles
st.markdown("""# :office: :incoming_envelope: :rainbow-background[Better Letter] :love_letter: :love_hotel:
## :violet-background[Summarize Official German Letters]

""")

# Allow user to upload several images
uploaded_images = st.file_uploader("You want to upload your photos of the letter?", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# Allow user to use their webcam
st.write("You want to use your webcam?")
if st.button('Toggle Webcam'):
    toggle_webcam()

if st.session_state.webcam_enabled:
    st.camera_input('')

# Display uploaded images and summary
if uploaded_images:
    display_uploaded_images(uploaded_images)
    display_summary()
