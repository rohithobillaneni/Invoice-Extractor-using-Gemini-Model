import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page Configuration
st.set_page_config(page_title="Invoice Extractor", page_icon="📄", layout="centered")

st.markdown("""
    <style>
        .stTextInput > div > div > input {
            font-size: 18px;
        }
        .stButton button {
            font-size: 18px;
            background-color: #2E8B57;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)


# Title Section
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>📄 Invoice Extractor using Gemini</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Upload an invoice image and ask natural language questions about it.<br>Try things like <i>'What is the total amount?'</i> or <i>'Who is the vendor?'</i></p>", unsafe_allow_html=True)
st.markdown("---")


# Sidebar: File Upload
with st.sidebar:
    st.markdown("### 🖼️ Upload Invoice Image")
    uploaded_file = st.file_uploader("Select an image file", type=["jpg", "jpeg", "png"])

# Display Uploaded Image
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🧾 Uploaded Invoice", use_container_width=True)

# Input Area
st.markdown("### 💬 Ask a Question")
input_text = st.text_input("Type your question about the invoice:", placeholder="e.g., What is the total amount?", label_visibility="collapsed")

# Prompt for Gemini
system_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices &
you will have to answer questions based on the input image.
"""

# Prepare image for Gemini
def input_image_setup(uploaded_file):
    if uploaded_file:
        return [{
            "mime_type": uploaded_file.type,
            "data": uploaded_file.getvalue()
        }]
    else:
        raise FileNotFoundError("No file uploaded.")

# Gemini API Call
def get_gemini_response(system_prompt, image_data, query):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([system_prompt, image_data[0], query])
    return response.text

# Submit Button
if st.button("🔍 Extract Information", use_container_width=True):
    if not uploaded_file:
        st.warning("⚠️ Please upload an invoice image.")
    elif not input_text.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("🔎 Analyzing the invoice..."):
            try:
                image_data = input_image_setup(uploaded_file)
                result = get_gemini_response(system_prompt, image_data, input_text)
                st.markdown("### ✅ Extracted Answer")
                st.markdown(f"<div style='font-size:18px; background-color:#f5f5f5; padding:15px; border-radius:10px;'>{result}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
