import streamlit as st

st.title('Mi primera aplicación con Streamlit')
st.write('¡Hola, Streamlit!')

'''
# Encabezado 1

## Encabezado 2

Cualquier texto en formato *negritas*, _cursivas_...
'''

nombre = st.text_input('Escribe tu nombre')
anio_nacimiento = st.slider('¿En qué año naciste?', 1940, 2024)
if anio_nacimiento > 1940:
    st.write(f'Tienes {2024 - anio_nacimiento} años')

# Botón
if len(nombre) > 0:
    if st.button('Saluda'):
        st.write(f'Hola {nombre}.')

color = st.selectbox(
    'Elige tu color favorito',
    ['rojo', 'verde', 'azul'],
    index=None,
    placeholder="Color...",)
if color != None:
    st.write(f'Tu color favorito es {color}.')

import pandas as pd

df = pd.DataFrame({
    'A' : [1, 2, 3, 4],
    'B' : ['a', 'b', 'c', 'd']
})

st.write(df)

import matplotlib.pyplot as plt

fig = plt.figure()
plt.scatter(df.A, df.B)
st.pyplot(fig)

archivo = st.file_uploader('Sube un archivo TXT', type = ['txt'])
texto = None
if archivo != None:
    texto = archivo.read().decode("utf-8")
    if texto:
        st.write(texto)

# Tarea 6

# Crear un formulario simple en streamlit que tome entrada del usuario y visualice los resultados en una tabla y un gráfico.
