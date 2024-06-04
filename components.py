import streamlit as st
from PIL import Image

def display_uploaded_image(uploaded_image):
    #for uploaded_image in uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Letter', use_column_width=True)

def display_summary(response):
    st.markdown("### Summary")
    # Dummy summary
    st.write(response)

# optional: allow user to select number of lines via slider
def allow_slider_line_count():
    line_count = st.slider('How many lines shall the summary have? ', 1, 10, 3)

# optional: have a horizontal display of the file uploader and camera input
def horizontal_input():
    col1, col2 = st.columns(2)

    with col1:
        uploaded_image = st.file_uploader("Upload your photos of the letter?", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

    with col2:
        enable_webcam = st.camera_input('Use your webcam?')
