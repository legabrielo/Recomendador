''' 
Aplicación hecha con streamlit 
'''




import streamlit as st
import pandas as pd
import numpy as np
import os 
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors
import pickle 


# Descargamos el dataframe 
print("Current Working Directory:", os.getcwd())
path_features = os.path.dirname(__file__)
features = path_features+'/features.csv'
path_features = os.path.dirname(__file__)
res = path_features+'/res.csv'

# Cargamos el modelo 
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the pickled model
model_path = os.path.join(script_dir, 'models', 'Modelo_Restaurantes.pkl')

# Load the pickled model
with open(model_path, 'rb') as model_file:
    modelo = pickle.load(model_file)


print(res.index.values)

def dar_restaurante(filtered_res):
            liked_restaurant = filtered_res.iloc[0]
            print(liked_restaurant)
            num_recom = 8
            _, ind = modelo.kneighbors(features.iloc[[liked_restaurant.name]])
        
            st.subheader('Recommended Restaurants')
            rec_indices = ind[0][0:num_recom]
            rec_resta = res.iloc[rec_indices, :]
            st.write(rec_resta)

def main():
    st.title("Recomendador Guía Michelin Madrid 2023")

    selected_style = st.selectbox("Seleccione estilo:", res['Estilo'].unique().astype(str))
    selected_price = st.selectbox("Seleccione precio:", res['Precio'].unique().astype(str))

    filtered_res = res[
        (res['Estilo'] == selected_style) &
        (res['Precio'] == selected_price) 
    ]

    
    print('This is filtered res:' '\n', filtered_res)
    # Añadir aquí un buclque para que primero pono ponga nada (done)

    if filtered_res.empty:
        if st.button("Obtener restaurantes"):
            st.write('No hay recomendación todavía')
    else:
        if st.button("Obtener restaurantes"):
            dar_restaurante(filtered_res)
         

        


if __name__ == "__main__":
    main()

