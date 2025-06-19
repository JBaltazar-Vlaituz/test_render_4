import streamlit as st
import pandas as pd
import plotly.express as px

# Título y bienvenida
st.title("Análisis interactivo de autos usados 🚗📊")
st.write("👋 ¡Bienvenido! Esta aplicación permite explorar datos reales de anuncios de autos en EE.UU.")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar una vista previa del dataset
st.subheader("🔍 Vista previa del dataset:")
st.dataframe(car_data.head())

# Gráfico que se muestra automáticamente al cargar la app
st.subheader("📊 Distribución inicial del precio de los autos")
fig_init = px.histogram(car_data, x='price', title="Distribución de precios")
st.plotly_chart(fig_init, use_container_width=True)

# Gráfico interactivo 1: Histograma
if st.button('Mostrar histograma de odómetro'):
    st.subheader('📉 Histograma de kilometraje (odómetro)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Gráfico interactivo 2: Scatter plot
if st.button('Mostrar gráfico de dispersión (odómetro vs precio)'):
    st.subheader('📈 Gráfico de dispersión: Odómetro vs Precio')
    fig = px.scatter(car_data, x='odometer', y='price', color='type')
    st.plotly_chart(fig, use_container_width=True)