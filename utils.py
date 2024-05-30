import streamlit as st

def toggle_webcam():
    st.session_state.webcam_enabled = not st.session_state.webcam_enabled
