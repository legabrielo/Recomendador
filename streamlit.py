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
# print("Current Working Directory:", os.getcwd())
features = pd.read_csv(r'features.csv')
res = pd.read_csv(r'res.csv')

# Cargamos el modelo 
modelo = pickle.load(open('Modelo_Restaurantes.pkl', 'rb'))


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

