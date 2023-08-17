''' 
Aplicación hecha con streamlit 
'''




import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors
import pickle 


# Descargamos el dataframe 
res = pd.read_csv(r'C:\Users\Gabriel Castillo\Desktop\Cosas Gabriel\ML Restaurantes\res.csv')
features = pd.read_csv(r'C:\Users\Gabriel Castillo\Desktop\Cosas Gabriel\ML Restaurantes\features.csv')

res = res.drop(columns='Unnamed: 0')

# Cargamos el modelo 
modelo = pickle.load(open(r'C:\Users\Gabriel Castillo\Desktop\Cosas Gabriel\ML Restaurantes\models\Modelo_Restaurantes.pkl', 'rb'))


print(res.index.values)

def main():
    st.title("Recomendador Guía Michelin Madrid 2023")

    # User inputs for preferences
    selected_style = st.selectbox("Seleccione estilo:", res['Estilo'].unique().astype(str))
    selected_price = st.selectbox("Seleccione precio:", res['Precio'].unique().astype(str))

    # Filter restaurants based on user preferences
    filtered_res = res[
        (res['Estilo'] == selected_style) &
        (res['Precio'] == selected_price) 
    ]

    print('This is filtered res:' '\n', filtered_res)
    
    st.button("Restaurantes Recomendados")
    num_recom = 4
    liked_restaurant = filtered_res.iloc[0]
    num_recom = 4
    _, ind = modelo.kneighbors(features.iloc[[liked_restaurant.name]])
    
    st.subheader('Recommended Restaurants')
    rec_indices = ind[0][0:num_recom]
    rec_resta = res.iloc[rec_indices, :]
    st.write(rec_resta)

    


if __name__ == "__main__":
    main()

