""" Esta aplicación estará basada en el modelo del recomendador que fue creado.
    Está entrenado con los datos de la guía Michelin del Año 2023 para la ciudad de Madrid. 
    El recomendador está basado en el uso de recomendadores de contenido para generar un primer resultado 

"""

import numpy as np
from flask import Flask, request, render_template 
import pickle 

# Creamos el objeto 
app = Flask(__name__)

# Cargamos el modelo 
modelo = pickle.load(open('ML Restaurantes/Modelo_Restaurantes.pkl', 'rb'))

@app.route('/')
def home():
    render_template('web_code.html')

@app.route('/recom', methods=['POST'])
def recom():
    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    recomendado = modelo

    return render_template('web_code.html', prediction_text = 'Restaurante Recomendado {}'.format(recomendado))


if __name__ == '__main__':
    app.run(debug=True)