import streamlit as st
from utils import toggle_webcam
from components import display_uploaded_image, display_summary
import requests
import time

#url = 'http://0.0.0.0:8000/summary_eng'
#url = 'https://light-ooqm7vogaa-ew.a.run.app/summary_eng'
# url = 'https://better-letter-api-4ipo33uimq-ew.a.run.app'
# url = 'https://lighttesseract-4ipo33uimq-uc.a.run.app/summary_eng'
url = 'https://lighttesseract-new-4ipo33uimq-ew.a.run.app//summary_eng'

# Initialize session state for webcam
if 'webcam_enabled' not in st.session_state:
    st.session_state.webcam_enabled = False

# Create titles
#st.markdown("""# :office: :incoming_envelope: :rainbow-background[Better Letter] :love_letter: :love_hotel:
## :violet-background[Summarize Official German Letters]


# Create titles
st.markdown("""# :incoming_envelope: BETTER LETTER """)
st.markdown(""" ---------- """)
st.markdown(""" ### Got a letter in German language?  Let's figure out what it says!""")

# sidebar
st.sidebar.image('https://postimg.cc/LJcdQtDk/deab52f9', use_column_width=True)

# Allow user to upload image
uploaded_image = st.file_uploader("You want to upload your photos of the letter?", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

# Allow user to use their webcam
st.write("You want to use your webcam?")
if st.button('Toggle Webcam'):
    toggle_webcam()

if st.session_state.webcam_enabled:
    st.camera_input('')

# Display progress bar after uploading image
if uploaded_image:
    uploaded_image_dict = {str(i): file for i, file in enumerate(uploaded_image)}

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    time.sleep(1)  # Simulate some work being done
    my_bar.progress(50, text="Halfway done...")

    time.sleep(1)  # Simulate more work being done
    my_bar.progress(100, text="Operation complete.")

    # Display uploaded image and summary
    display_uploaded_image(uploaded_image)

    # request to API
    img = uploaded_image.getvalue()
    files = {'file': img}
    response = requests.post(url, files=files).json()
    #display_summary(response)
    display_summary(response['summary'])
