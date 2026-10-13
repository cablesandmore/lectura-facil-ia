import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Leer API Key
api_key = os.getenv("GEMINI_API_KEY")

# Configurar Gemini
genai.configure(api_key=api_key)

# Modelo
model = genai.GenerativeModel("gemini-3.8-flash")

# Interfaz
st.title("Lectura Fácil IA")

texto = st.text_area(
    "Pega aquí un texto administrativo"
)

if st.button("Simplificar"):

    prompt = f"""
    Convierte el siguiente texto a lectura fácil.

    Utiliza frases cortas.
    Evita tecnicismos.
    Mantén el significado original.

    Texto:

    {texto}
    """

    respuesta = model.generate_content(prompt)

    st.subheader("Versión simplificada")
    st.write(respuesta.text)