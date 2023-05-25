class Nodo:
    def __init__(self, x, y, padre=None):
        self.x = x
        self.y = y
        self.padre = padre

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        return self.items.pop(0)

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar(self, x, y, padre=None):
        nodo = Nodo(x, y, padre)
        if self.esta_vacia():
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.padre is not None:
                actual = actual.padre
            actual.padre = nodo

    def obtener_camino(self):
        camino = []
        actual = self.cabeza
        while actual is not None:
            camino.append((actual.x, actual.y))
            actual = actual.padre
        camino.reverse()
        return camino

def resolver_abra(x_inicial, y_inicial, x_final, y_final):
    movimientos = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    visitados = set()
    cola = Cola()
    cola.encolar(Nodo(x_inicial, y_inicial))
    while not cola.esta_vacia():
        actual = cola.desencolar()
        if actual.x == x_final and actual.y == y_final:
            camino = ListaEnlazada()
            while actual is not None:
                camino.agregar(actual.x, actual.y, actual.padre)
                actual = actual.padre
            return camino.obtener_camino()
        for dx, dy in movimientos:
            x_nuevo = actual.x + dx
            y_nuevo = actual.y + dy
            if 1 <= x_nuevo <= 4 and 1 <= y_nuevo <= 3 and (x_nuevo, y_nuevo) not in visitados:
                visitados.add((x_nuevo, y_nuevo))
                cola.encolar(Nodo(x_nuevo, y_nuevo, actual))
    return None

def main():
    # Ejemplo de uso
    x_inicial, y_inicial = 1, 1
    x_final, y_final = 4, 3
    camino = resolver_abra(x_inicial, y_inicial, x_final, y_final)
    if camino is not None:
        print(f'Se encontró un camino de longitud {len(camino)}:')
        for x, y in camino:
            print(f'({x}, {y})')
    else:
        print('No se encontró un camino válido.')

if __name__ == '__main__':
    main()