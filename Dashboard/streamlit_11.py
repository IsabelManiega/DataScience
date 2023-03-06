import streamlit as st
import yfinance as yf
import plotly.express as px

st.set_page_config(layout="wide")

# titulo
st.title("Gráfica con streamlit para finanzas")

# seleccion una emopresa de ellas:
empresas = ("GOOGL", "AAPL", "TSLA", "NFLX")
opcion = st.selectbox("Selecciona un de estas empresas: ",
                      empresas)
st.write("Has elegido: ", opcion)

# 1 año a 5 de 1 en 1 para este ejemplo:
anho = st.slider("Numero de años que quieres plotear: ",
                 1, 5, 1)
st.write("Has elegido: ", anho)

anho_final = 2015 + anho
st.write("año final: ", anho_final, ' años')

# Obtención de datos via quandl:
data = yf.download(opcion, "2015-1-1", f'{anho_final}-12-31')

# head
st.write("Vamos a imprimir los 5 primeros valores del dataset")
st.write(data.head())

# # tambien como dataframe
# st.dataframe(data.head())

# tail
st.write("Vamos a imprimir los 5 últimos valores del dataset")
st.write(data.tail())

columns = tuple(data.columns)

# elegimos la columna
radio = st.radio("selecciona una columna: ", columns)
data_col = data[[radio]]
st.write(data_col)

# Visualización usando plotly:
data = data.rename_axis("Date").reset_index()
fig = px.line(data, x=data["Date"], y=data[radio],
              title=f"Cotización de {radio}")
st.plotly_chart(fig, use_container_width=True)
