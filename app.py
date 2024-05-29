import streamlit as st
from PIL import Image


# Create titles
st.markdown("""# 	:office: :incoming_envelope: :rainbow-background[Better Letter] :love_letter: :love_hotel:
## :violet-background[Summarize Official German Letters]
""")

# Allow user to select number of lines via slider
# line_count = st.slider('How many lines shall the summary have? ', 1, 10, 3)

# Allow user to upload several images
uploaded_images = st.file_uploader("You want to upload your photos of the letter?", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# enable use of user webcam
enable_webcam = st.camera_input('You want to use your webcam?', help)

# Display uploaded images and summary
if uploaded_images:
    for uploaded_image in uploaded_images:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Letter', use_column_width=True)

    st.markdown(f"### Summary ({line_count} lines)")
    # Dummy summary
    dummy_summary = "This is a dummy summary of the letter. " * line_count
    st.write(dummy_summary)
