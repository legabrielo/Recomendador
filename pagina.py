""" Esta aplicación estará basada en el modelo del recomendador que fue creado.
    Está entrenado con los datos de la guía Michelin del Año 2023 para la ciudad de Madrid. 
    El recomendador está basado en el uso de recomendadores de contenido para generar un primer resultado 

"""

import numpy as np
from flask import Flask, request, render_template 
import pickle 
import pandas as pd 
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier

# Creamos el objeto 
app = Flask(__name__)

# Cargamos el modelo 
modelo = pickle.load(open(r'C:\Users\Gabriel Castillo\Desktop\Cosas Gabriel\ML Restaurantes\models\Modelo_Restaurantes.pkl', 'rb'))

# Descargamos el dataframe 
restau = pd.read_csv(r'C:\Users\Gabriel Castillo\Desktop\Cosas Gabriel\ML Restaurantes\res.csv')
features = pd.read_csv(r'C:\Users\Gabriel Castillo\Desktop\Cosas Gabriel\ML Restaurantes\features.csv')

@app.route('/')
def home():
    return render_template('web_code.html')

@app.route('/recom', methods=['POST'])
def recom():
    int_features = [int(x) for x in request.form.values()]
    numero = [np.array(int_features)]
    dif, ind = modelo.kneighbors(features.iloc[numero[0]])
    indices_recomendados = restau.loc[ind[0][1:5], :]  # Obtener los índices de los restaurantes recomendados
    
    # Convertir el dataframe a HTML
    recomendados_html = indices_recomendados.to_html()
    
    # Renderizar el template 'web_code.html' y pasar los datos de los restaurantes recomendados a la plantilla
    return render_template('web_code.html', prediction_text = recomendados_html)

if __name__ == "__main__":
    app.run()       