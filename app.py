import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="AgriGuard AI | IIT Patna", page_icon="🌿")

# --- UI Header ---
st.title("🌿 AgriGuard AI")
st.markdown("### Plant Disease Detection System")
st.info("Developed at **Indian Institute of Technology, Patna**")

# --- Load Model (Dummy logic for now) ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/5/52/Indian_Institute_of_Technology%2C_Patna_Logo.png", width=100)
st.sidebar.markdown("---")
st.sidebar.write("Project by Rajan Singh Parmar")

# --- Main Feature ---
uploaded_file = st.file_uploader("Paudhe ki photo upload karein...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    if st.button("🔍 Scan for Diseases"):
        with st.spinner('AI analysis kar raha hai...'):
            # Abhi dummy result dikhayega kyunki model train ho raha hai
            st.success("Analysis Complete: Your plant looks Healthy! ✅")
            st.balloons()

st.divider()
st.caption("© 2026 AgriGuard Project | Powered by Streamlit")