def n_pokeballs(n):
    # Inicializar el tablero vacío
    tablero = [[' ' for _ in range(n)] for _ in range(n)]

    # Función auxiliar para colocar las pokeballs
    def colocar_pokeball(fila, tablero):
        # Si se han colocado todas las pokeballs, se ha encontrado una solución
        if fila == n:
            return True

        # Probar a colocar una pokeball en cada columna de la fila actual
        for col in range(n):
            # Comprobar si la pokeball se puede colocar en esta posición
            if es_posicion_segura(fila, col, tablero):
                # Colocar la pokeball en esta posición
                tablero[fila][col] = 'O'

                # Llamar recursivamente a la función para colocar la siguiente pokeball
                if colocar_pokeball(fila + 1, tablero):
                    return True

                # Si no se ha encontrado una solución, quitar la pokeball de esta posición
                tablero[fila][col] = ' '

        # Si no se ha encontrado una solución, devolver False
        return False

    # Función auxiliar para comprobar si una posición es segura
    def es_posicion_segura(fila, col, tablero):
        # Comprobar si hay otra pokeball en la misma columna
        for i in range(fila):
            if tablero[i][col] == 'O':
                return False

        # Comprobar si hay otra pokeball en la misma diagonal hacia arriba
        i = fila - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if tablero[i][j] == 'O':
                return False
            i -= 1
            j -= 1

        # Comprobar si hay otra pokeball en la misma diagonal hacia abajo
        i = fila - 1
        j = col + 1
        while i >= 0 and j < n:
            if tablero[i][j] == 'O':
                return False
            i -= 1
            j += 1

        # Si no hay ninguna pokeball en la misma columna ni en las mismas diagonales, la posición es segura
        return True

    # Llamar a la función auxiliar para colocar las pokeballs
    colocar_pokeball(0, tablero)

    # Devolver el tablero con la solución
    return tablero

def main():
    for n in range(1, 16):
        solucion = n_pokeballs(n)
        print(f'Solución para {n} pokeballs:')
        for fila in solucion:
            print(' '.join(fila))
        print()

if __name__ == '__main__':
    main()