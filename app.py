import streamlit as st

import numpy as np
import pandas as pd


# create titles
st.markdown("""# Better Letter
## Summarize and Simplify Official German Letters
Just take a photo of the letter, load it here and understand everything.""")

# allow user to upload image
uploaded_image = st.file_uploader("Upload a photo of the letter", type=["png", "jpg", "jpeg"])

# st.camera_input

# display uploaded image
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Letter', use_column_width=True)


# allow user to select number of lines via slider
line_count = st.slider('How many lines shall the summary have? ', 1, 10, 3)

# display placeholder for summary
if uploaded_image is not None:
    st.markdown(f"### Summary ({line_count} lines)")
    # Dummy summary - in a real application, you would replace this with the actual summary logic
    dummy_summary = "This is a dummy summary of the letter." * line_count
    st.write(dummy_summary)
