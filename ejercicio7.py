class NodoHuffman:
    def __init__(self, simbolo=None, frecuencia=0, izquierda=None, derecha=None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

class Heap:
    def __init__(self):
        self.datos = []

    def agregar(self, elemento):
        self.datos.append(elemento)
        self._flotar(len(self.datos) - 1)

    def obtener_minimo(self):
        minimo = self.datos[0]
        ultimo = self.datos.pop()
        if self.datos:
            self.datos[0] = ultimo
            self._hundir(0)
        return minimo

    def _flotar(self, indice):
        padre = (indice - 1) // 2
        if indice > 0 and self.datos[indice] < self.datos[padre]:
            self.datos[indice], self.datos[padre] = self.datos[padre], self.datos[indice]
            self._flotar(padre)

    def _hundir(self, indice):
        hijo_izquierdo = 2 * indice + 1
        hijo_derecho = 2 * indice + 2
        minimo = indice
        if hijo_izquierdo < len(self.datos) and self.datos[hijo_izquierdo] < self.datos[minimo]:
            minimo = hijo_izquierdo
        if hijo_derecho < len(self.datos) and self.datos[hijo_derecho] < self.datos[minimo]:
            minimo = hijo_derecho
        if minimo != indice:
            self.datos[indice], self.datos[minimo] = self.datos[minimo], self.datos[indice]
            self._hundir(minimo)

def construir_arbol_huffman(tabla_frecuencias):
    heap = Heap()
    for simbolo, frecuencia in tabla_frecuencias.items():
        heap.agregar(NodoHuffman(simbolo, frecuencia))

    while len(heap.datos) > 1:
        nodo_izquierda = heap.obtener_minimo()
        nodo_derecha = heap.obtener_minimo()
        nuevo_nodo = NodoHuffman(frecuencia=nodo_izquierda.frecuencia + nodo_derecha.frecuencia, izquierda=nodo_izquierda, derecha=nodo_derecha)
        heap.agregar(nuevo_nodo)

    return heap.obtener_minimo()

def codificar_mensaje(arbol_huffman, mensaje):
    tabla_codigos = {}
    codificar_recursivo(arbol_huffman, "", tabla_codigos)
    mensaje_codificado = ""
    for caracter in mensaje:
        mensaje_codificado += tabla_codigos[caracter]
    return mensaje_codificado

def codificar_recursivo(nodo, codigo_actual, tabla_codigos):
    if nodo.simbolo is not None:
        tabla_codigos[nodo.simbolo] = codigo_actual
    else:
        codificar_recursivo(nodo.izquierda, codigo_actual + "0", tabla_codigos)
        codificar_recursivo(nodo.derecha, codigo_actual + "1", tabla_codigos)

def decodificar_mensaje(arbol_huffman, mensaje_codificado):
    mensaje_decodificado = ""
    nodo_actual = arbol_huffman
    indice = 0
    while indice < len(mensaje_codificado):
        bit = mensaje_codificado[indice]
        if bit == "0":
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha
        if nodo_actual.simbolo is not None:
            mensaje_decodificado += nodo_actual.simbolo
            nodo_actual = arbol_huffman
        indice += 1
    return mensaje_decodificado

def main():
    tabla_frecuencias = {
        "T": 0.15/1.09,
        "O": 0.15/1.09,
        "A": 0.12/1.09,
        "E": 0.10/1.09,
        "H": 0.09/1.09,
        "S": 0.07/1.09,
        "P": 0.07/1.09,
        "M": 0.07/1.09,
        "N": 0.06/1.09,
        "C": 0.06/1.09,
        "D": 0.05/1.09,
        "Z": 0.04/1.09,
        "K": 0.03/1.09,
        ",": 0.03/1.09
    }
    arbol_huffman = construir_arbol_huffman(tabla_frecuencias)
    mensaje = "TONA,CAE"
    mensaje_codificado = codificar_mensaje(arbol_huffman, mensaje)
    mensaje_decodificado = decodificar_mensaje(arbol_huffman, mensaje_codificado)
    print("Mensaje original: ", mensaje)
    print("Mensaje codificado: ", mensaje_codificado)
    print("Mensaje decodificado: ", mensaje_decodificado)

if __name__ == "__main__":
    main()