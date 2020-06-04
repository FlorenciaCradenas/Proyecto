import modules.search as pt
grafo = {
    'A': ['M', 'N', 'S'],
    'B': ['J','V','X','Z'],
    'C': ['D','M','S'],
    'D': ['C'],
    'E': ['F','O'],
    'F': ['E','H','Y'],
    'G': ['P','T','X','Z'],
    'H': ['F','X'],
    'J': ['B','O','Y'],
    'M': ['A','C'],
    'N': ['A','O'],
    'O': ['E','J','N','V'],
    'P': ['G','T','U'],
    'S': ['A','C','V'],
    'T': ['G','P'],
    'U': ['P','X'],
    'V': ['B','O','S'],
    'X': ['B','G','H','U','Z'],
    'Y': ['F','J'],
    'Z': ['B','G','X'],
}
# inicio = input('Dame la ciudad de origen')
# destino = input('Dame la ciudad de destino')
# p = pt.busqueda(map, 'X' , 'V')
# print(p)
# h = pt.amplitud(map, 'X', 'V')
# print(h)

p = pt.busqueda(grafo, 'X', 'Z')
# print(p)