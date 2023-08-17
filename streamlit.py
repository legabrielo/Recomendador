''' 
Aplicación hecha con streamlit 
'''




import streamlit as st
import pandas as pd
import numpy as np
import sklearn
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
    # st.subheader('Restaurante elegido')
    print(liked_restaurant)
    num_recom = 4
    _, ind = modelo.kneighbors(features.iloc[[liked_restaurant.name]])
    st.subheader('Recommended Restaurants')
    rec_indices = ind[0][0:num_recom]
    rec_resta = res.iloc[rec_indices, :]
    st.write(rec_resta)

    


if __name__ == "__main__":
    main()

  # Get recommendations using NearestNeighbors
            # Cambiamos el tipo de dataframe 
            # filtered_array = np.asarray(filtered_res)
            # print('This is filtered array:', filtered_array)
            # filtered_array_numpy = filtered_array.reshape(1,-1)
            # print('This is filtered array numpy:', filtered_array_numpy)
            # _, ind = modelo.kneighbors(features.iloc[filtered_array_numpy])

            # # Print statements for troubleshooting
            # print("Indices array:", ind)  # Print the content of the indices array
            
            # recommended_indices = ind[1][1:]  # Skip the first index since it's the liked restaurant
            # print("Recommended indices:", recommended_indices)  # Print the recommended indices
            
            # st.subheader('Liked Restaurant')
            # st.write("=" * 60)
            # liked_index = recommended_indices[0]
            # res.iloc[filtered_array_numpy[liked_index], :]

            # st.subheader('Recommended Restaurants')
            # st.write("=" * 60)
            # recommended_restaurants = res.loc[filtered_array_numpy[recommended_indices], :]
            # st.write(recommended_restaurants)