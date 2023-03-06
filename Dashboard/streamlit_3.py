import streamlit as st

check = st.checkbox("Me encanta Python")

if check:
    st.write("Buena elección")
else:
    st.write("¿Estás seguro?, deberías replanteártelo")
