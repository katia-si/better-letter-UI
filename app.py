import streamlit as st
from utils import toggle_webcam
from components import display_uploaded_images, display_summary
import requests
import time

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

# Display progress bar after uploading images
if uploaded_images:
    uploaded_images_dict = {str(i): file for i, file in enumerate(uploaded_images)}

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    time.sleep(1)  # Simulate some work being done
    my_bar.progress(50, text="Halfway done...")

    time.sleep(1)  # Simulate more work being done
    my_bar.progress(100, text="Operation complete.")

    # Display uploaded images and summary
    display_uploaded_images(uploaded_images)


    # request to API
    for image in uploaded_images:
        img = image.getvalue()
        files = {'file': img}
        response = requests.post('https://light-ooqm7vogaa-ew.a.run.app/summary_eng', files=files).json()

    display_summary(response['summary'])

# https://light-ooqm7vogaa-ew.a.run.app/summary_eng
