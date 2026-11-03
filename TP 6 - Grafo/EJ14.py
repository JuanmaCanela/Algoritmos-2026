# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas: 
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

from graph import Graph

grafo = Graph(is_dir=False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
grafo.add_vertex('cocina')
grafo.add_vertex('comedor')
grafo.add_vertex('cochera')
grafo.add_vertex('quincho')
grafo.add_vertex('baño 1')
grafo.add_vertex('baño 2')
grafo.add_vertex('habitación 1')
grafo.add_vertex('habitación 2')
grafo.add_vertex('sala de estar')
grafo.add_vertex('terraza')
grafo.add_vertex('patio')

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
grafo.add_edge(4, 'sala de estar', 'comedor')
grafo.add_edge(9, 'sala de estar', 'habitación 1')
grafo.add_edge(7, 'sala de estar', 'habitación 2')
grafo.add_edge(4, 'sala de estar', 'baño 1')
grafo.add_edge(8, 'sala de estar', 'terraza')
grafo.add_edge(5, 'patio', 'cocina')
grafo.add_edge(6, 'patio', 'quincho')
grafo.add_edge(9, 'patio', 'cochera')
grafo.add_edge(4, 'patio', 'terraza')
grafo.add_edge(7, 'patio', 'comedor')
grafo.add_edge(3, 'comedor', 'cocina')
grafo.add_edge(5, 'habitación 1', 'habitación 2')
grafo.add_edge(3, 'habitación 1', 'baño 1')
grafo.add_edge(4, 'habitación 2', 'baño 2')
grafo.add_edge(6, 'baño 1', 'baño 2')
grafo.add_edge(5, 'quincho', 'cochera')
grafo.add_edge(8, 'quincho', 'cocina')
grafo.add_edge(7, 'cochera', 'cocina')
grafo.add_edge(10, 'baño 2', 'terraza')

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
print()
print('-----C-----')
print()

arbol = grafo.kruskal('cocina')
print(arbol)

metros = 0

for arista in arbol.split(';'):
    metros += int(arista.split('-')[-1])

print()
print("Metros de cable necesarios:", metros)

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
print()
print('-----D-----')
print()

print("Camino mas corto desde habitacion 1 hasta sala de estar:")

caminos = grafo.dijkstra('habitación 1')

destino = 'sala de estar'
camino = []
metros = 0

while caminos.size() > 0:
    dato = caminos.pop()

    if dato[0] == destino:
        metros = dato[1]
        camino.append(dato[0])
        destino = dato[2]

camino.reverse()

print("Camino:", " -> ".join(camino))
print()
print("Metros de cable necesarios:", metros)