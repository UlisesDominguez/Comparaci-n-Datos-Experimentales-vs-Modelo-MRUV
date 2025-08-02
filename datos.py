import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from physics import calcular_posicion_mruv

def cargar_datos():
    """Carga datos experimentales desde un archivo CSV local"""
    ds = pd.read_csv("datos_.csv")  # Asegúrate de que este archivo esté en el mismo directorio
    return ds

st.title("Comparación: Datos Experimentales vs Modelo MRUV")

try:
    ds = cargar_datos()
    st.success("Datos cargados correctamente.")
    st.dataframe(ds)

    # Entradas para el modelo
    x0 = st.number_input("Posición inicial (m)", value=0.0)
    v0 = st.number_input("Velocidad inicial (m/s)", value=0.0)
    a = st.number_input("Aceleración (m/s²)", value=9.8)

    # Cálculo teórico
    ds["pos_teorica"] = ds["tiempo"].apply(lambda t: calcular_posicion_mruv(x0, v0, a, t))

    # Gráfico comparativo
    fig, ax = plt.subplots()
    ax.plot(ds["tiempo"], ds["posicion"], 'o-', label="Datos experimentales")
    ax.plot(ds["tiempo"], ds["pos_teorica"], 'r--', label="Modelo teórico")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Posición (m)")
    ax.set_title("MRUV: Modelo vs Datos")
    ax.legend()
    st.pyplot(fig)