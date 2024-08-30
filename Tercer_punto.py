def leer_matriz(filas, columnas):
    """
    Lee una matriz del usuario, validando que cada fila tenga el número correcto de columnas.
    """
    matriz = []
    print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")
    for i in range(filas):
        while True:
            try:
                fila = list(map(int, input(f"Fila {i+1} (separada por espacios): ").split()))
                if len(fila) != columnas:
                    print(f"Error: La fila debe tener {columnas} elementos. Inténtalo de nuevo.")
                    continue
                matriz.append(fila)
                break
            except ValueError:
                print("Error: Entrada inválida. Asegúrate de ingresar números separados por espacios.")
    return matriz

def imprimir_matriz(matriz):
    """
    Imprime una matriz de manera legible.
    """
    for fila in matriz:
        print(" ".join(map(str, fila)))

def transponer_matriz(matriz):
    """
    Calcula la matriz transpuesta.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_transpuesta = [[0] * filas for _ in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[j][i] = matriz[i][j]
    return matriz_transpuesta

def main():
    print("Transposición de matrices")
    
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    
    print("Ingrese la matriz:")
    matriz = leer_matriz(filas, columnas)
    
    print("\nMatriz ingresada:")
    imprimir_matriz(matriz)
    
    print("\nMatriz transpuesta:")
    matriz_transpuesta = transponer_matriz(matriz)
    imprimir_matriz(matriz_transpuesta)

if __name__ == "__main__":
    main()
