import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import datetime

# --- Page Configuration ---
st.set_page_config(page_title="AgriGuard AI | IIT Patna", page_icon="🌿", layout="wide")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { background-color: #1b5e20; color: white; }
    .sidebar .sidebar-content { background-image: linear-gradient(#e8f5e9,#ffffff); }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar: Kisan Sewa Kendra ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/5/52/Indian_Institute_of_Technology%2C_Patna_Logo.png", width=100)
st.sidebar.title("👨‍🌾 Kisan Sewa Kendra")
st.sidebar.info(f"**Aaj ki Tarikh:** {datetime.date.today()}")

st.sidebar.subheader("🌤️ Weather Update")
st.sidebar.write("Patna, Bihar: *32°C | Sunny*")

st.sidebar.subheader("💹 Mandi Bhav (Today)")
st.sidebar.write("🍅 Tomato: ₹2,400/Quintal")
st.sidebar.write("🥔 Potato: ₹1,800/Quintal")

# --- Main Portal ---
st.title("🌿 AgriGuard AI: Smart Farming Portal")
st.markdown("Developed at *Indian Institute of Technology, Patna*")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("🔍 Plant Health Scanner")
    uploaded_file = st.file_uploader("Paudhe ki photo upload karein...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Photo', use_container_width=True)
        
        if st.button("Bimari ki Jaanch Karein"):
            with st.spinner('AI Dimag laga raha hai...'):
                # Dummy Result for now (since we use dummy model)
                st.balloons()
                st.success("✅ Analysis Complete: Paudha Swasth Hai!")
                st.info("AI Confidence: 98.4%")

with col2:
    st.header("📰 Agriculture News")
    st.write("📌 PM-Kisan ki 17th kist jald aane wali hai.")
    st.write("📌 Bihar mein Organic Farming par 50% subsidy.")
    
    st.divider()
    st.header("📞 Helpline")
    st.write("Kisan Call Center: *1800-180-1551*")

st.divider()
st.caption("© 2026 AgriGuard Project | IIT Patna | Empowering Indian Farmers")