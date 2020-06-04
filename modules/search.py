import queue
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


def busqueda(map, inicio, destino) -> ty.List[float]:
    arbol.append(inicio)
    while arbol:
        ciudad = arbol.pop()
        if inicio == destino:
            return destino
        if ciudad not in recorrido and ciudad != inicio:
            recorrido.append(ciudad)
            print(recorrido)
        for key in map[ciudad]:
            print(key)
            if key not in recorrido:
                recorrido.append(key)
                print(recorrido)



def ruta(st_1: list) -> list:
    lst = []
    lst.append(busqueda(map, inicio, destino))
    print(lst)
#
# def invert(lst_1: list) -> list:
#     if not lst_1:
#         return lst_1
#     else:
#         return [lst_1[-1]] + invert(lst_1[:-1])
#
#
# def result_function(n: int) -> ty.List[float]:
#     lst = []
#     for n in range(0, n + 1):
#         lst.append(function_math(n))
#         print(lst[n], end=' ')
#     return lst
