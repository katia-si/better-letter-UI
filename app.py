import streamlit as st
from utils import toggle_webcam
from components import display_uploaded_image
import requests

url = 'https://lighttesseract-new-4ipo33uimq-ew.a.run.app/summary_eng'

# Set page configuration to hide the sidebar by default
st.set_page_config(
    page_title="Better Letter",
    page_icon=":incoming_envelope:",
    layout="centered",  # Centered layout
    initial_sidebar_state="collapsed",  # Hide sidebar by default
)

# Initialize session state for webcam
if 'webcam_enabled' not in st.session_state:
    st.session_state.webcam_enabled = False

# Create titles
st.markdown("# :incoming_envelope: BETTER LETTER")
st.markdown("----------")
st.markdown("### Got a letter in German language?  Let's figure out what it says!")

# Sidebar
st.sidebar.image('https://postimg.cc/LJcdQtDk/deab52f9', use_column_width=True)

# Allow user to upload image
uploaded_image = st.file_uploader("You want to upload your photos of the letter?", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

# Allow user to use their webcam
st.write("You want to use your webcam?")
if st.button('Toggle Webcam'):
    st.session_state.webcam_enabled = not st.session_state.webcam_enabled

if st.session_state.webcam_enabled:
    webcam_image = st.camera_input('')  # Capture webcam image

# Function to process and display image
def process_image(image):
    if image:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        # Request to API
        img = image.getvalue()
        files = {'file': img}

        try:
            response = requests.post(url, files=files)
            response.raise_for_status()  # Check for HTTP request errors
            summary = response.json().get('summary', 'No summary found.')
            my_bar.progress(100, text="Operation complete.")

            # Centering the summary
            st.markdown('<p style="text-align:center; font-size: 22pt"> -- Summary -- </p>', unsafe_allow_html=True)
            st.markdown(
                f"""
                <div style="text-align:center; border:2px solid #4CAF50; padding: 20px; border-radius: 10px; background-color: #f9f9f9; font-size: 18pt; color: black;">
                    {summary}
                </div>
                """,
                unsafe_allow_html=True
            )
        except requests.exceptions.RequestException as e:
            my_bar.progress(0, text="Operation failed.")
            st.error(f"Error: {e}")

# Display uploaded image and process uploaded image
if uploaded_image:
    display_uploaded_image(uploaded_image)
    if st.button("Summarize it"):  # Button to show the summary
        process_image(uploaded_image)

# Process webcam image
st.markdown('<hr style="height:3px;">', unsafe_allow_html=True)  # Add a larger horizontal line
if st.session_state.webcam_enabled and 'webcam_image' in locals():
    if st.button("Summarize it"):  # Button to show the summary
        process_image(webcam_image)
