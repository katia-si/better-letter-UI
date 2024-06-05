import streamlit as st

st.markdown("""
# Welcome to Better Letter!

This project aims to assist users in understanding the contents of official German letters by providing a web interface to upload images of these letters and receive English summaries. This is achieved through a series of backend processes, including OCR (Optical Character Recognition), text cleaning, summarization, and translation.

## User Interface

The user interface is built using Streamlit. It allows users to upload images of their letters or use a webcam to capture them. The backend processes the image, extracts the text, cleans it, summarizes it, and translates the summary into English.

## How to Use

1. **Access the Application**: Navigate to the Better Letter web app on https://better-letter.streamlit.app.
2. **Upload an Image**: You can either upload an image of the letter in PNG, JPG, or JPEG format, or use your webcam to capture the image directly.
3. **Processing**: Once the image is uploaded, the app will display a progress bar indicating the processing status.
4. **View Summary**: After processing, the app will display the extracted text's summary in English.

## Project Structure

The project consists of three repositories: one for the main processing repo, one for the user interface, and one for the API.
""")
