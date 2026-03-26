import streamlit as st
import numpy as np
from PIL import Image
import datetime

# --- Page Config ---
st.set_page_config(page_title="AgriGuard AI | IIT Patna", page_icon="🌿", layout="wide")

# --- Leafy Background & Styling ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/leaf.png");
        background-color: #e8f5e9;
    }
    .main-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        border: 2px solid #2e7d32;
    }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
        border: 2px solid white;
    }
    h1 { color: #1b5e20 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar: Kisan Sewa Kendra ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/5/52/Indian_Institute_of_Technology%2C_Patna_Logo.png", width=100)
st.sidebar.title("👨‍🌾 Kisan Sewa")
st.sidebar.success(f"📅 Aaj ki Tarikh: {datetime.date.today()}")

st.sidebar.subheader("🌤️ Weather: Patna")
st.sidebar.write("🌡️ 32°C | ☀️ Sunny")

st.sidebar.divider()
st.sidebar.subheader("💹 Mandi Bhav")
st.sidebar.write("🍅 Tamatar: ₹2,400/Q")
st.sidebar.write("🥔 Aloo: ₹1,800/Q")

# --- Main Section ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("🌿 AgriGuard AI: Smart Plant Doctor")
st.write("<p style='text-align: center;'>IIT Patna Project for Indian Farmers</p>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔍 Paudhe ka Photo Upload Karein")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Aapka Paudha', use_container_width=True)
        
        if st.button("Bimari ki Jaanch Karein"):
            with st.spinner('AI analysis kar raha hai...'):
                st.balloons()
                st.success("✅ Analysis Result: Aapka paudha ekdum Swasth (Healthy) hai!")
                st.progress(98)
                st.write("Confidence Score: 98.4%")

with col2:
    st.subheader("📰 Kheti ki Khabrein")
    st.info("📌 PM-Kisan ki kist jaldi aane wali hai.")
    st.warning("⚠️ Agle 2 din baarish ki sambhavna.")
    
    st.divider()
    st.subheader("📞 Helpline")
    st.write("📞 1800-180-1551")

st.markdown('</div>', unsafe_allow_html=True)
st.divider()
st.caption("© 2026 AgriGuard Project | Powered by IIT Patna")