import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import datetime

# --- Page Config (IIT Patna Theme) ---
st.set_page_config(page_title="AgriGuard AI | IIT Patna", page_icon="🌿", layout="wide")

# --- Custom Styling (Mandi Style) ---
st.markdown("""
    <style>
    .main { background-color: #f4f7f1; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 8px; font-weight: bold; }
    .mandi-card { background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar: User Info & Weather ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/5/52/Indian_Institute_of_Technology%2C_Patna_Logo.png", width=80)
st.sidebar.title("👨‍🌾 Kisan Sewa Kendra")
st.sidebar.info(f"Aaj ki Tarikh: {datetime.date.today()}")
# --- Logo aur Header Section ---
col1, col2 = st.columns([1, 5]) # Logo ke liye choti column aur title ke liye badi

with col1:
    # Aap niche wale URL ko apne kisi bhi logo URL se badal sakte hain
    st.image("https://upload.wikimedia.org/wikipedia/en/5/52/Indian_Institute_of_Technology%2C_Patna_Logo.png", width=100)

with col2:
    st.title("🌿 AgriGuard AI: Smart Farming")
    st.markdown("#### Indian Institute of Technology, Patna")

st.divider()

# Dummy Weather/Mandi Data
st.sidebar.markdown("### 🌤️ Weather Update")
st.sidebar.write("Patna, Bihar: **32°C | Sunny**")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💹 Mandi Bhav (Today)")
st.sidebar.write("🍅 Tomato: ₹2,400/Quintal")
st.sidebar.write("🥔 Potato: ₹1,800/Quintal")

# --- Main UI ---
st.title("🌿 AgriGuard AI: Smart Farming Portal")
st.markdown("Developed at **Indian Institute of Technology, Patna**")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🔍 Plant Health Scanner")
    uploaded_file = st.file_uploader("Paudhe ki photo upload karein...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width=True)
        
        if st.button("Analyze Fasal"):
            # Dummy Logic for now
            st.warning("Analysis: **Early Blight Detected ⚠️**")
            
            # --- Added Treatment Suggestions (Like Pro Websites) ---
            st.markdown("### 💊 Upchar (Treatment)")
            st.success("""
            * **Dawai:** Mancozeb (2g/Litre) ka chidkaw karein.
            * **Sallah:** Khrab patto ko turant tod kar jala dein.
            * **Savadhaani:** Agli baar fasal chakr (Crop Rotation) apnayein.
            """)

with col2:
    st.markdown("### 📰 Agriculture News")
    st.info("📌 PM-Kisan ki 17th kist jald aane wali hai.")
    st.info("📌 Bihar mein Organic Farming par 50% subsidy.")
    
    st.markdown("### 📞 Helpline")
    st.write("Kisan Call Center: **1800-180-1551**")

st.divider()
st.caption("© 2026 AgriGuard Project | IIT Patna | Empowering Indian Farmers")