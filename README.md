# Recomendador
Este es el prototipo para un recomendador de la guía Michelin en Madrid. 

Los datos han sido recolectados con Selenium como principal librería para hacer el Webscrap. 

Para generar el Recomendador se intentaron dos maneras: 
  1. Intentamos hacer el recomendador con un filtrado colaborativo, como se ve en el notebook en la parte de "Matrix". Este estaba pensado generando datos artificiales de 5 supuestos usuarios que han visitado los restaurantes del webscrap. Después se intentó usar la distancia del coseno para poder buscar las distancias entre cada usuario. 
  2. La siguiente manera fue utilizando un One Hot Encoder para usar un algoritmo supervisado de Kneighbors. Utilizando el estilo de comida y el precio de los restaurantes usamos el OHE para crear carateristicas y que el algoritmo las pueda identificar. 

Para el html utilizamos un template muy básico que simplemente pide que pongas el número del restaurante que visitaste. 

*Nota* -- La idea es mejorar como se ve la página para que sea mas atractivo al usuario y se vean los restaurantes para que la gente sepa cuál fue al que acudió. 

Para el despliegue del recomendador se uso flask.

## Próximas actualizaciones:

### Front end:
   1. Intentaré mejorar la página básica de HTML para que sea más user friendly. Colores más bonitos y que la recomendación dada se pueda entender :)
   2. Que la respuesta se vea de mejor manera.
### Back end:
   1. Buscar otro sistema para desplegar en la web el recomendador (Más que todo para cuando haga el post en LinkedIn)
   2. Dudando si cambiar las métricas para hacer la recomendación (Hay otras variables que hay que tener en cuenta : Si el usuario es nuevo, los features, la distancia etc)

   
