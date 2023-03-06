import streamlit as st

opcion = st.selectbox("Tu lenguaje de programación favorito",
                      ("Python", "C++", "Matlab"))

st.write("Seleccionaste: ", opcion)