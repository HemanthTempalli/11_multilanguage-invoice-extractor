# Q&A Chatbot using Google Gemini Pro Vision
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables (like your API key)
load_dotenv()

# Get the Google API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("❌ GOOGLE_API_KEY not found in environment variables.")
    st.stop()

# Configure Gemini with the API key
genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(system_prompt, image_data, user_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model
    response = model.generate_content([system_prompt, image_data[0], user_prompt])
    return response.text


# Function to prepare image data for Gemini
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI setup
st.set_page_config(page_title="Gemini Invoice Q&A")
st.header("🧾 Gemini Invoice Chatbot")

# Input fields
user_question = st.text_input("💬 Ask a question about the invoice image (e.g., 'What is the total amount?')", key="input")
uploaded_file = st.file_uploader("📂 Upload an invoice image", type=["jpg", "jpeg", "png"])

# Show uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_container_width=True)

# System prompt for Gemini
system_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices,
and you must answer questions based on the input image.
"""

# Submit button
if st.button("🔍 Tell me about the image"):
    if not uploaded_file:
        st.warning("⚠️ Please upload an image before submitting.")
    elif not user_question.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(system_prompt, image_data, user_question)
        st.subheader("📄 Response")
        st.write(response)
