from collections import deque
import typing as ty

map = {
    'A': ['N', 'S', 'M'],
    'B': ['Z', 'X', 'J', 'V'],
    'C': ['D', 'M', 'S'],
    'D': ['C'],
    'E': ['F', 'O'],
    'F': ['E', 'H', 'Y'],
    'G': ['T', 'P', 'X', 'Z'],
    'H': ['F', 'X'],
    'J': ['B', 'Y', 'O'],
    'M': ['C', 'A'],
    'N': ['O', 'A'],
    'O': ['N', 'V', 'J', 'E'],
    'P': ['T', 'G', 'U'],
    'S': ['C', 'A', 'V'],
    'T': ['P', 'G'],
    'U': ['P', 'X'],
    'V': ['B', 'O', 'S'],
    'X': ['U', 'H', 'G', 'Z', 'B'],
    'Y': ['F', 'J'],
    'Z': ['G', 'X', 'B'],
}

arbol = []
recorrido = []

def busqueda(map, inicio, destino)-> ty.List[float]:
    arbol.append(inicio)
    recorrido.append(inicio)
    if inicio == destino:
        return destino
    while arbol:
        ciudad = arbol.pop()
        if ciudad not in recorrido:
            recorrido.append(ciudad)
            return busqueda(map, inicio, ciudad)
        for key in map[ciudad]:
            if key not in recorrido:
                arbol.append(key)
                recorrido.append(key)
    return recorrido

