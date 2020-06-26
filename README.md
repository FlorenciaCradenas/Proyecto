# BÚSQUEDAS EN AMPLITUD

# Introducción
Para dar pie al tema, iniciemos definiendo qué son las "Búsquedas". 
Las búsquedas, son una técnica para resolver problemas, en donde se examinan las posibles secuencias que conduzcan a valores conocidos y así, poder elegir la mejor de estas.

Alguna vez en nuestra vida hemos estado frente a la interrogante: "¿Qué camino debo elegir para llegar a cierto lugar?"
Este proyecto trata de resolver dicha interrogante mediante la implementación de **_búsquedas de amplitud_**, con el propósito de determinar cual ruta se debe seguir para ir de un punto inicial hasta llegar a nuestro destino.  Este tipo de algoritmo es de particular importancia en varios problemas de decisión, donde lo que se requiere es encontrar una solución o probar que no existe ninguna solución.



# Metodología
La búsqueda en amplitud es un recorrido de grafo (usado frecuentemente en árboles) en donde se toma el nodo raíz, después sus sucesores, expandiendo todos los nodos a una profundidas en el árbol de búsqueda antes de expandir cualquier nodo del próximo nivel, en este tipo de busqueda la estructura de datos empleada es **Fifo** es decir primero en entrar, primero en salir. 

En este caso supongamos que nos encontramos en la ciudad de Xalapa, y queremos llegar a San Andrés Tuxtla, apoyados del siguiente mapa:

![Imagen del mapa](Mapa.png)


Lo que hará nuestro programa es determinar el nodo raíz, en este caso es Xalapa, seguido de expandir los sucesores del nodo raíz (vecinos de Xalapa) los cuales vemos que son: _Teziutlan_, _Huatusco_, _Vega de Alatorre_, _Zempoala_ y _Boca del rio_, como ninguna ciudad es el destino volvemos a expandir nuestros nodos comenzando desde por los vecinos de Boca del Río sin repetir los nodos ya analizados. los vecinos de Boca del rio son _Joachin_ y  _Alvarado_ y nuevamente ninguno es el destino ni en los demas vecinos de las ciudades de Teziutlan, Huatusco ,  Vega de Alatorre y Zempoala_  por ende volvemos a expandir los nodos  de Alvarado asi se tiene _Otatitlan_ y _San Andrés Tuxtla_ nos damos cuenta que ya encontramos nuestro destino, entonces la ruta a seguir es: _Xalapa, Boca del Rio, Alvarado y San Andés Tuxtla_. 

El desarrollo sería de la siguiente forma:

![Imagen ejemplo](Pruebas/Ejemplo.png)


En este pequeño ejemplo nos dimos cuenta cómo trabaja un algoritmo de búsqueda en amplitud.
El lenguaje de programación implementado es **Python**, trabajando con el algoritmo:
![Imagen del algoritmo](algoritmo.png)

Nosotras elaboramos el siguiente programa:

![Imagen del programa](programa.png)

Como podemos notar el codigo se apoya de dos funciones, la funcion _ruta_ y la función _busqueda_ en la cual se expanden los nodos apoyado del siguiente diccionario:

![Imagen del Diccionario](diccionario.png)

Donde las claves de las ciudades estn determinadas por la siguiente lista:

![Imagen de la Lista de las ciudades](lista.png)

Entonces la función busqueda agrega en una lista llamada arbol el nodo raiz "inicio" y se agrega tambien en un diccionario llamado recorrido el nodo inicial y el valor None, que quiere decir que dicho nodo no tiene antecesores. Se emplea un ciclo _while_ el cual contiene los demas ciclos, en dicho ciclo se pregunta si la lista arbol no es vacia continua asignando a la variable ciudad lo que se saca de la lista arbol, ademas se pregunta si la ciudad es el destino retornamos a la funcion _ruta_ la cual imprime el camino a seguir, posteriormente en el ciclo _for_ es el encargado de expandir los nodos ya que verifica los vecinos de nuestras ciudades, y las agrega a la lista arbol y a la cola recorrido con su valor antecesor de esta manera se hace un cliclo hasta llegar a nuestro destino.
Las estructuras de datos implementadas son listas y diccionarios principalmente por el control de los datos que tenemos ya que en un diccionario podemos agregar un dato y su valor, esto es necesario para agregar los vecinos y sus antesesores. 

Cabe destacar que en nuestro programa afecta la forma de acomodar los datos de nuestro diccionario llamado "mapa" ya que los nodos se expanderian de distinta manera. 



# Experimentos

![Prueba1](Pruebas/A-H.png)


![Prueba2](Pruebas/F-P.png)



![Prueba3](Pruebas/H-A.png)




![Prueba4](Pruebas/J-M.png)



![Prueba5](Pruebas/X-B.png)




![Prueba6](Pruebas/X-V.png)





