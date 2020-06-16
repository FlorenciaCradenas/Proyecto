import queue
import typing as ty


arbol = []
recorrido = {}

def busqueda(map, inicio, destino) -> ty.List[float]:
    arbol.append(inicio)
    recorrido.setdefault(inicio, None)
    while arbol:
        ciudad = arbol.pop()
        if ciudad == destino:
            return ruta(recorrido, ciudad)
        for key in map[ciudad]:
            if key not in recorrido:
                arbol.append(key)
                recorrido.setdefault(key, ciudad)




def ruta(recorrido, ciudad) -> list:
    if recorrido[ciudad] == None:
        return [ciudad]
    else:
        return ruta(recorrido, recorrido[ciudad]) + [ciudad]
