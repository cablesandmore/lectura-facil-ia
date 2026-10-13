import streamlit as st

st.title("Lectura Fácil IA")

texto = st.text_area(
	"Pega aquí un texto administrativo"
)

if st.button("Simplificar"):
	st.write(
		"Aquí aparecerá el texto simplificado"
	)
