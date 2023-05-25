class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = {}
        self.pesos = {}

    def agregar_vertice(self, valor):
        self.vertices.add(valor)

    def agregar_arista(self, desde, hasta, peso):
        if desde not in self.aristas:
            self.aristas[desde] = []
        if hasta not in self.aristas:
            self.aristas[hasta] = []
        self.aristas[desde].append(hasta)
        self.aristas[hasta].append(desde)
        self.pesos[(desde, hasta)] = peso

    def mst_kruskal(self):
        aristas_ordenadas = sorted(self.pesos.items(), key=lambda x: x[1])
        arbol = Grafo()
        for v in self.vertices:
            arbol.agregar_vertice(v)
        conjunto_vertices = {v: {v} for v in self.vertices}
        for arista, peso in aristas_ordenadas:
            v1, v2 = arista
            conjunto1 = conjunto_vertices[v1]
            conjunto2 = conjunto_vertices[v2]
            if conjunto1 != conjunto2:
                arbol.agregar_arista(v1, v2, peso)
                conjunto_union = conjunto1.union(conjunto2)
                for v in conjunto_union:
                    conjunto_vertices[v] = conjunto_union
        return arbol

def main():
    # Crear el grafo de tareas
    tareas = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'A', 'B', 'C', 'D', 'E', 'F']
    grafo = Grafo()
    for tarea in tareas:
        grafo.agregar_vertice(tarea)

    grafo.agregar_arista('G', 'H', 25)
    grafo.agregar_arista('G', 'M', 25)
    grafo.agregar_arista('H', 'J', 25)
    grafo.agregar_arista('H', 'M', 25)
    grafo.agregar_arista('I', 'J', 35)
    grafo.agregar_arista('J', 'K', 15)
    grafo.agregar_arista('J', 'M', 25)
    grafo.agregar_arista('K', 'L', 5)
    grafo.agregar_arista('A', 'D', 20)
    grafo.agregar_arista('A', 'E', 20)
    grafo.agregar_arista('A', 'F', 10)
    grafo.agregar_arista('B', 'C', 40)
    grafo.agregar_arista('B', 'E', 5)
    grafo.agregar_arista('C', 'E', 5)
    grafo.agregar_arista('D', 'M', 10)
    grafo.agregar_arista('E', 'F', 10)

    # Calcular el MST del grafo
    mst = grafo.mst_kruskal()

    # Imprimir la secuencia de tareas en el MST
    print("Árbol de expansión mínima de las tareas: ")
    for arista, peso in mst.pesos.items():
        v1, v2 = arista
        print(v1, '->', v2)

if __name__ == '__main__':
    main()