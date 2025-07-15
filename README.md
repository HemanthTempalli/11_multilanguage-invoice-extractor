# 📄 Gemini Invoice Q&A Chatbot

A Streamlit web application that uses **Google Gemini 1.5 Flash** to understand and answer questions about uploaded **invoice images**. Supports invoices in **multiple languages** thanks to Gemini's multimodal and multilingual capabilities.

---

## 🚀 Features

- 🧠 Powered by Gemini 1.5 Flash (Google's multimodal AI)
- 📸 Upload invoice images (JPG, PNG)
- 💬 Ask natural language questions like:
  - "What is the total amount?"
  - "Who issued the invoice?"
  - "When is the due date?"
- 🌍 Works with invoices in multiple languages
- 📦 Lightweight Streamlit interface

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Generative AI Python SDK](https://pypi.org/project/google-generativeai/)
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini)
- `python-dotenv` for secure API key loading
- `Pillow` for image handling

---

## 📦 Installation

1. **Clone this repo**:
   ```bash
   git clone https://github.com/yourusername/gemini-invoice-qa.git
   cd gemini-invoice-qa
