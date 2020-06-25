# BÚSQUEDAS EN AMPLITUD

# Introducción
Para dar pie al tema, iniciemos definiendo qué son las "Búsquedas". 
Las búsquedas, son una técnica para resolver problemas, en donde se examinan las posibles secuencias que conduzcan a valores conocidos y así, poder elegir la mejor de estas.

Alguna vez en nuestra vida hemos estado frente a la interrogante: "¿Qué camino debo elegir para llegar a cierto lugar?"
Este proyecto trata de resolver dicha interrogante mediante la implementación de **_búsquedas de amplitud_**, con el propósito de determinar cual ruta se debe seguir para ir de un punto inicial hasta llegar a nuestro destino. 



# Metodología
La búsqueda en amplitud es un recorrido de grafo (usado frecuentemente en árboles) en donde se toma el nodo raíz, después sus sucesores, expandiendo todos los nodos a una profundidas en el árbol de búsqueda antes de expandir cualquier nodo del próximo nivel. 

En este caso supongamos que nos encontramos en la ciudad de Xalapa, y queremos llegar a San Andrés Tuxtla, apoyados de siguiente mapa: 

![Imagen del mapa](Mapa.png)

Lo que hará nuestro programa es determinar el nodo raíz, en este caso es Xalapa, seguido de expandir los sucesores del nodo raíz (vecinos de Xalapa) los cuales vemos que son: _Teziutlan_, _Huatusco_, _Vega de Alatorre_, _Zempoala_ y _Boca del rio_, como ninguna ciudad es el destino volvemos a expandir nuestros nodos comenzando desde el último nodo sin repetir las ciudades, es decir, buscamos los vecinos de Boca del Río sin repetir los nodos ya analizados. los vecinos de Boca del rio son _Joachin_ y  _Alvarado_ y nuevamente ninguno es el destino por ende volvemos a expandir los nodos de Alvarado asi se tiene _Otatitlan_ y _San Andrés Tuxtla_ nos damos cuenta que ya encontramos nuestro destino, entonces la ruta a seguir es: _Xalapa, Boca del Rio, Alvarado y San Andés Tuxtla_. 

En este pequeño ejemplo nos dimos cuenta cómo trabaja un algoritmo de búsqueda en amplitud. Este tipo de algoritmo es de particular importancia en varios problemas de decisión, donde lo que se requiere es encontrar una solución o probar que no existe ninguna solución.

![Imagen del algoritmo](algoritmo.png)

# Experimentos




