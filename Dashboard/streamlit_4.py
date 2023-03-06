import streamlit as st

radio = st.radio(("Tener en cuenta los Outliers"),
                 ("Si", "No"))

if radio == "Si":
    st.write("No eliminaremos los Outliers del Dataset")
else:
    st.write("Eliminaremos los Outliers del Dataset")