import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Bienvenido a mi primer aplicacion de analisis de vehiculos")

vehicles_data = pd.read_csv('vehicles_us.csv') #lee el archivo con datos
hist_check = st.checkbox ('Construir histograma', key = 'histogram_checkbox') #Crea el boton para un histograma
disp_check = st.checkbox ('Construir grafico de dispersion', key = 'disp_checkbox') #Crea el boton para un grafico de dispersion

if hist_check: #al hacer clic en el boton
    #haz esto:
    st.write ('Creacion de un histograma para el conjunto de datos de anuncios de venta de autos')

    #Crea el filtro para mostrar dentro del actuador checbox bajo las opciones mostradas con un selectbox
    select_model = st.selectbox('Selecciona el modelo de auto', options= vehicles_data['type'].unique(), key = 'histogram_selectbox')
    filtered_data = vehicles_data[vehicles_data['type'] == select_model] #filtro para tomar los datos de la columna 'type' que muestran los modelos de los autos

    #crear hist
    fig_hist = px.histogram(filtered_data, x= "odometer")

    #muestra un grafico interactivo plotly
    st.plotly_chart(fig_hist, use_container_width = True)

if disp_check: #si el chechbox se presiona...

    #muestra el mensaje siguiente
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de autos')

     #Crea el filtro para mostrar dentro del actuador checbox bajo las opciones mostradas con un selectbox
    select_model_disp = st.selectbox('Selecciona el modelo de auto', options= vehicles_data['type'].unique(), key = 'scatter_selectbox')
    filtered_data_disp = vehicles_data[vehicles_data['type'] == select_model_disp]

    #crea el grafico de dispersion
    fig_scatter = px.scatter(filtered_data_disp, x = "odometer", y = "price")

    #muestra un codigo interactivo para un grafico de dispersion con odometer y price como titulos de x y y
    st.plotly_chart(fig_scatter, use_container_width= True)