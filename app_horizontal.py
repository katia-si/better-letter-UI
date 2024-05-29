import streamlit as st
from PIL import Image

# Create titles
st.markdown("""# 	:office: :incoming_envelope: :rainbow-background[Better Letter] :love_letter: :love_hotel:
## :violet-background[Summarize Official German Letters]
""")

# Allow user to select number of lines via slider
line_count = st.slider('How many lines shall the summary have? ', 1, 10, 3)

# Create columns for file uploader and camera input
col1, col2 = st.columns(2)

with col1:
    uploaded_images = st.file_uploader("Upload your photos of the letter?", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

with col2:
    enable_webcam = st.camera_input('Use your webcam?')

# Display uploaded images and summary
if uploaded_images:
    for uploaded_image in uploaded_images:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Letter', use_column_width=True)

    st.markdown(f"### Summary ({line_count} lines)")
    # Dummy summary
    dummy_summary = "This is a dummy summary of the letter. " * line_count
    st.write(dummy_summary)
