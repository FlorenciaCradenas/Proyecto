# BUSQUEDAS EN AMPLITUD

# Introducción
Alguna vez en nuestra vida hemos estado frente a la inerroante ¿Qué camino debo elegir para llegar a cierto lugar?.
Este proyecto trata de resolver dicha interrogante mediante la implementación de **_busquedas en amplitud_**, con el proposito de determinar que ruta se debe seguir para ir de un ponto inicial hasta llear a nuestro destino. Pero ¿qué son las busquedas en amplitud?

Búsqueda en amplitud es un algoritmo para recorrer o buscar elementos de un grafo(usado frecuentemente en arboles) en la que se expande primero el nodo raíz, a continuación se expanden todos los sucesores del nodo raíz, después sus sucesores, etc. En general, se expanden todos los nodos a una profundidad en
el árbol de búsqueda antes de expandir cualquier nodo del próximo nivel. En este caso supongamos que nos encontramos en la ciudades de xalapa, y queremos llegar a San andres tuxtla,apoyados de siguiente mapa (pner mapa) 
Entonces lo que hará nuestro programa es determinar el nodo raíz que en este caso es Xalapa, seguido de expandir los sucesores del nodo raíz (vecinos de xalapa) los cuales vemos que son _Teziutlan_, _Huatusco_, _Vega de Alatorre_, _Zempoala_ y _Boca del rio_, como ninguna ciudad es el destino volvemos a expandir nuestros nodos comenzando desde el último nodo sin repetri las ciudades, es decir buscamos los vecinos de boca del rio sin repetir los nodos ya analizados. Vemos que los vecinos de Boca del rio son _Joachin_ y  _Alvarado_ y nuevamente ninguno es el destino por ende volvemos a expandir los nodos de Alvarado asi se tiene _Otatitlan_ y _San Andrés Tuxtla_ nos damos cuenta que ya encontramos nuestro destino, entonces la ruta a seguir es: _Xalapa, Boca del Rio, Alvarado y San Andés Tuxtla_. 

En este pequeño ejemplo nos dimos cuenta como trabaja un aloritmo de busqueda en amplitud. Este tipo de algoritmo es de particular importancia en varios problemas de decisión, donde lo que se requiere es encontrar una solución o probar que no existe ninguna solución.

![Imagen del algoritmo](algoritmo.png)
