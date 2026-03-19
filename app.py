import streamlit as st
import os
from dotenv import load_dotenv
from agent.crop_agent import analyze_crop
from utils.image_utils import validate_image
from config.settings import APP_NAME, APP_TAGLINE, SUPPORTED_FORMATS

load_dotenv()

st.set_page_config(page_title=APP_NAME, page_icon="🌱", layout="centered")
st.title(f"🌱 {APP_NAME}")
st.caption(APP_TAGLINE)

uploaded_file = st.file_uploader("Upload a photo of your plant or leaf", type=SUPPORTED_FORMATS)

location = st.text_input("Your location", placeholder="e.g. Kano, Nigeria")

farmer_note = st.text_area("Anything else?", placeholder="e.g. Leaves started turning yellow 3 days ago", height=80)

if st.button("Analyze Crop 🔍"):
    if not uploaded_file:
        st.warning("Please upload a photo first.")
    else:
        file_bytes = uploaded_file.read()
        valid, msg = validate_image(file_bytes, uploaded_file.name)
        if not valid:
            st.error(msg)
        else:
            with st.spinner("Analyzing your crop..."):
                result = analyze_crop(file_bytes, farmer_note=farmer_note, location=location)
            st.markdown("---")
            st.markdown("### Analysis")
            st.markdown(result)

st.markdown("---")
st.caption("CropAdvisor - For smallholder farmers - Powered by AI")