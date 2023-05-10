class Vertice:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.adyacente = {}

    def agregar_vecino(self, vecino, peso=1):
        self.adyacente[vecino] = peso

    def obtener_conexiones(self):
        return self.adyacente.keys()

    def __str__(self):
        return f"{self.nombre}: {self.adyacente}"


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def agregar_vertice(self, nombre, tipo):
        self.num_vertices += 1
        nuevo_vertice = Vertice(nombre, tipo)
        self.vertices[nombre] = nuevo_vertice
        return nuevo_vertice

    def agregar_arista(self, desde, hasta, peso=1):
        if desde not in self.vertices:
            self.agregar_vertice(desde)
        if hasta not in self.vertices:
            self.agregar_vertice(hasta)
        self.vertices[desde].agregar_vecino(self.vertices[hasta], peso)
        self.vertices[hasta].agregar_vecino(self.vertices[desde], peso)

    def dijkstra(self, inicio, objetivo):
        import heapq

        dist = {vertice: float('inf') for vertice in self.vertices}
        dist[inicio] = 0

        pq = [(0, inicio)]

        while pq:
            distancia_actual, vertice_actual = heapq.heappop(pq)

            if distancia_actual > dist[vertice_actual]:
                continue

            for vecino, peso in self.vertices[vertice_actual].adyacente.items():
                distancia = distancia_actual + peso

                if distancia < dist[vecino.nombre]:
                    dist[vecino.nombre] = distancia
                    heapq.heappush(pq, (distancia, vecino.nombre))

        return dist[objetivo]

# Creación del grafo y de sus vértices
g = Grafo()

estaciones = ["King's Cross", "Waterloo", "Estación de Tren de Victoria", "Estación de Liverpool Street", "St. Pancras", "Paddington"]
empalmes = [str(i) for i in range(1, 13)]

for estacion in estaciones:
    g.agregar_vertice(estacion, 'estacion')

for empalme in empalmes:
    g.agregar_vertice(empalme, 'empalme')

# Conexiones entre los vértices
g.agregar_arista("King's Cross", '1')
g.agregar_arista('1', '2')
g.agregar_arista('2', '3')
g.agregar_arista('3', 'Waterloo')
g.agregar_arista('Estación de Tren de Victoria', '4')
g.agregar_arista('4', '5')
g.agregar_arista('5', '6')
g.agregar_arista('6', 'Estación de Liverpool Street')
g.agregar_arista('St. Pancras', '7')
g.agregar_arista('7', '8')
g.agregar_arista('8', "King's Cross")

# Encuentra el camino más corto
print("Camino más corto de King's Cross a Waterloo:", g.dijkstra("King's Cross", 'Waterloo'))
print("Camino más corto de Estación de Tren de Victoria a Estación de Liverpool Street:", g.dijkstra('Estación de Tren de Victoria', 'Estación de Liverpool Street'))
print("Shortest path from St. Pancras to King's Cross:", g.dijkstra('St. Pancras', "King's Cross"))
