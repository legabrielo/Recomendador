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

# Cargamos el modelo 
modelo = pickle.load(open(r'C:\Users\Gabriel Castillo\Desktop\Cosas Gabriel\ML Restaurantes\models\Modelo_Restaurantes.pkl', 'rb'))



def main():
    st.title("Recomendador Guía Michelin Madrid 2023")

    # User inputs for preferences
    selected_style = st.selectbox("Select a style:", res['Estilo'].unique())
    selected_price = st.selectbox("Select a price range:", res['Precio'].unique())
    selected_stars = st.selectbox("Select the desired stars:", res['Estrellas Michelin'].unique())
    
    # Filter restaurants based on user preferences
    filtered_res = res[
        (res['Estilo'] == selected_style) &
        (res['Precio'] == selected_price) &
        (res['Estrellas Michelin'] == selected_stars)
    ]

    if st.button("Get Recommendations"):
        if not filtered_res.empty:
            # Get recommendations using NearestNeighbors
            indices = filtered_res.index
            dif, ind = modelo.kneighbors(features.iloc[indices])
            
            st.subheader('Liked Restaurant')
            st.write("=" * 60)
            st.write(res.loc[indices[ind[0][0]], :])

            st.subheader('Recommended Restaurants')
            st.write("=" * 60)
            st.write(res.loc[indices[ind[0][1:4]], :])
        else:
            st.write("No restaurants match your preferences.")

if __name__ == "__main__":
    main()
