import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from physics import calcular_posicion_mruv  # Asegúrate de tener este archivo y función

def cargar_datos():
    """
    Carga datos desde un archivo CSV local llamado 'dataset_algebra.csv'.
    El archivo debe tener columnas: tiempo,posicion.
    """
    ds = pd.read_csv("datos.csv")
    return ds

# Título de la aplicación
st.title("Comparación: Datos Experimentales vs Modelo MRUV")

# Bloque principal
try:
    # Cargar los datos
    ds = cargar_datos()
    st.success("Datos cargados correctamente.")
    st.dataframe(ds)

    # Entradas para el modelo teórico
    x0 = st.number_input("Posición inicial (m)", value=0.0)
    v0 = st.number_input("Velocidad inicial (m/s)", value=0.0)
    a = st.number_input("Aceleración (m/s²)", value=9.8)

    # Calcular posición teórica usando MRUV
    ds["pos_teorica"] = ds["tiempo"].apply(lambda t: calcular_posicion_mruv(x0, v0, a, t))

    # Gráfico de comparación
    fig, ax = plt.subplots()
    ax.plot(ds["tiempo"], ds["posicion"], 'o-', label="Datos experimentales")
    ax.plot(ds["tiempo"], ds["pos_teorica"], 'r--', label="Modelo teórico")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Posición (m)")
    ax.set_title("MRUV: Comparación entre Datos y Modelo")
    ax.legend()
    st.pyplot(fig)