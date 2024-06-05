import streamlit as st
from utils import toggle_webcam
from components import display_uploaded_image, display_summary
import requests
import time

url = 'https://lighttesseract-new-4ipo33uimq-ew.a.run.app/summary_eng'

def toggle_webcam():
    st.session_state.webcam_enabled = not st.session_state.webcam_enabled


# Set page configuration to hide the sidebar by default
st.set_page_config(
    page_title="Better Letter",
    page_icon=":incoming_envelope:",
    layout="centered",
    initial_sidebar_state="collapsed",  # Hide sidebar by default
)

# Initialize session state for webcam
if 'webcam_enabled' not in st.session_state:
    st.session_state.webcam_enabled = False

# Create titles
st.markdown("# :incoming_envelope: BETTER LETTER")
st.markdown("----------")
st.markdown("### Got a letter in German language?  Let's figure out what it says!")

# Allow user to upload image
uploaded_image = st.file_uploader("You want to upload your photos of the letter?", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

# Allow user to use their webcam
st.write("You want to use your webcam?")
if st.button('Toggle Webcam'):
    st.session_state.webcam_enabled = not st.session_state.webcam_enabled  # Modify session state toggle

if st.session_state.webcam_enabled:
    webcam_image = st.camera_input('')  # Capture webcam image

# Function to process and display image
def process_image(image):  # New function to process both types of images
    if image:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        time.sleep(1)  # Simulate some work being done
        my_bar.progress(50, text="Halfway done...")

        time.sleep(1)  # Simulate more work being done
        my_bar.progress(100, text="Operation complete.")

        # Display uploaded image and summary
        display_uploaded_image(image)

        # Request to API
        img = image.getvalue()
        files = {'file': img}
        response = requests.post(url, files=files).json()
        display_summary(response['summary'])

# Process uploaded image
if uploaded_image:
    process_image(uploaded_image)  # Process uploaded image

# Process webcam image
if st.session_state.webcam_enabled and webcam_image:
    process_image(webcam_image)  # Process webcam image
