import queue
import typing as ty


arbol = []
recorrido = {}

def busqueda(map, inicio, destino) -> ty.List[float]:
    arbol.append(inicio)
    recorrido.setdefault(inicio, None)
    while arbol:
        ciudad = arbol.pop()
        if inicio == destino:
            return ruta(recorrido, ciudad)
        for key in map[ciudad]:
            if key not in recorrido:
                arbol.append(key)
                recorrido.setdefault(key, ciudad)
                print(recorrido)



def ruta(recorrido, ciudad) -> list:
    for temp in recorrido:
        ciudad = temp
        print(ciudad)
        print(recorrido[ciudad])
    return [ciudad[-1]] + ruta(ciudad[:-1])
