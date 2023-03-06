import streamlit as st

# entrada texto
entrada_texto = st.text_input("Inserte text: ")
st.write("Texto del text_input: ", entrada_texto)

# entrada de números
entrada_numero = st.number_input("Inserte un numero")
st.write("Número del number_input: ", entrada_numero)