import modules.search as pt
mapa = {
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
    'X': ['U','H','G','Z','B'],
    'Y': ['F','J'],
    'Z': ['B','G','X'],
}
p = pt.busqueda(mapa, 'X','V')
print(p)
# recorrido = {
#  'A': None,
#  'Z': 'A',
#  'T': 'A',
#  'S': 'A',
#  'O': 'Z',
#  'L': 'T',
#  'F': 'S',
#  'R': 'S',
#  'M': 'L',
#  'B': 'F'
# }
#
# for temp in recorrido:
#     ciudad = temp
#     print(ciudad)
#     print(recorrido[ciudad])
