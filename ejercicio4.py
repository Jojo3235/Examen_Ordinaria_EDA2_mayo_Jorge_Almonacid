def contar_teletransportes_validos(n, k):
    # Definir las rutas disponibles
    rutas = [0, 1, 2, 3, 4, 6, 7, 8, 9]

    # Inicializar la matriz dp
    dp = [[0 for _ in range(10)] for _ in range(k+1)]
    for i in rutas:
        dp[0][i] = 1

    # Calcular los valores de dp utilizando programación dinámica
    for j in range(1, k+1):
        for i in rutas:
            if i == 0:
                dp[j][i] = dp[j-1][6] + dp[j-1][8]
            elif i == 1:
                dp[j][i] = dp[j-1][7] + dp[j-1][9]
            elif i == 2:
                dp[j][i] = dp[j-1][4] + dp[j-1][8]
            elif i == 3:
                dp[j][i] = dp[j-1][0] + dp[j-1][4] + dp[j-1][9]
            elif i == 4:
                dp[j][i] = dp[j-1][2] + dp[j-1][3] + dp[j-1][9]
            elif i == 6:
                dp[j][i] = dp[j-1][0] + dp[j-1][1] + dp[j-1][7]
            elif i == 7:
                dp[j][i] = dp[j-1][2] + dp[j-1][6]
            elif i == 8:
                dp[j][i] = dp[j-1][0] + dp[j-1][2]
            elif i == 9:
                dp[j][i] = dp[j-1][1] + dp[j-1][3]

    # Calcular la suma de todos los valores de dp[k][i]
    total = sum(dp[k][i] for i in rutas)

    return total

def main():
    casos = [1, 2, 3, 5, 8, 10, 15, 18, 21, 23, 32]
    for n in casos:
        for k in range(1, 4):
            solucion = contar_teletransportes_validos(n, k)
            print(f'Para n={n} y k={k}, la cantidad de posibles teletransportes válidos es {solucion}.')

if __name__ == '__main__':
    main()