import modules.search as pt
map = {
    'A': ['N', 'S', 'M'],
    'B': ['Z','X','J','V'],
    'C': ['D','M','S'],
    'D': ['C'],
    'E': ['F','O'],
    'F': ['E','H','Y'],
    'G': ['T','P','X','Z'],
    'H': ['F','X'],
    'J': ['B','Y','O'],
    'M': ['C','A'],
    'N': ['O','A'],
    'O': ['N','V','J','E'],
    'P': ['T','G','U'],
    'S': ['C','A','V'],
    'T': ['P','G'],
    'U': ['P','X'],
    'V': ['B','O','S'],
    'X': ['U','H','G','Z','B'],
    'Y': ['F','J'],
    'Z': ['G','X','B'],
}
# inicio = input('Dame la ciudad de origen')
# destino = input('Dame la ciudad de destino')
p = pt.busqueda(map, 'X', 'V')
print(p)
# h = pt.amplitud(map, 'X', 'V')
# print(h)