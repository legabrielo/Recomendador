# Recomendador Guía Michelin

Este es el prototipo para un recomendador de la guía Michelin en Madrid. 
Hay 2 propuestas para este recomendador. 

  **1.** El primer recomendador se desplegó con Flask. Inicialmente este era que se utilizaría para la publicación de LinkedIn pero me encontré con problemas a la hora de mostrarlo en Internet. Los códigos para este recomendador son web_code.html, pagina.py . En estos se puede ver el proceso con selenium, la creación del OHE y del filtrado colaborativo para ver cómo hacer el proyecto.
     
  **2.** El segundo recomendador se desplegó en Streamlit. Tomé esta decisión después de buscar nuevas alternativas para compartir de manera más fácil el proyecto. Se añadieron nuevas características para que los usuarios pudiesen personalizar la selección de comensales, estilo de comida, precio y evento (que era la idea original). Se mejoró la 




## Así se creó el Recomendador en Flask: 

  **1.** Se hizo un Webscrap de la página de la Guía Michelin en Madrid con la librería Selenium. 
  **2.** Desarollamos el recomendador con un filtrado colaborativo, como se ve en el notebook en la parte de "Matrix". Esta "Matrix" se conformó usando datos artificiales de 5 supuestos usuarios que han visitado los restaurantes. Después se tuvo en consideración la distancia del coseno para poder buscar las similitudes entre cada usuario. 
  **3.** La siguiente manera fue utilizando un One Hot Encoder para usar un algoritmo supervisado de Kneighbors. Utilizando el estilo de comida y el precio de los restaurantes usamos el OHE para crear carateristicas y que el algoritmo las pueda identificar.
  **4.** Creamos el código en Python para el despliegue de Flask. 
  **5.** Creamos un template básico de HTML que simplemente pide que pongas el número del restaurante que visitaste. A este template le añadimos un link a este repositorio y algunas imágenes de los restaurantes. 

## Así se hizo el Recomendador en Streamlit: 

  **1.** Se hizo un Webscrap de la página de la Guía Michelin en Madrid con la librería Selenium. 
  
## Próximas actualizaciones:

### Front end:
   1. Intentaré mejorar la página básica de HTML para que sea más user friendly. Colores más bonitos y que la recomendación dada se pueda entender :) (Listo)
   2. Que la respuesta se vea de mejor manera. (listo)
      
### Back end:
   1. Se va a cambiar de Flask a Streamlit
   2. Dudando si cambiar las métricas para hacer la recomendación (Hay otras variables que hay que tener en cuenta : Si el usuario es nuevo, los features, la distancia etc)

   
