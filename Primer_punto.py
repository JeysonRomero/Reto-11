def leer_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")
    for i in range(filas):
        fila = list(map(int, input(f"Fila {i+1} (separada por espacios): ").split()))
        if len(fila) != columnas:
            print(f"Error: La fila debe tener {columnas} elementos.")
            return None
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_suma = [[0] * columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matriz_suma[i][j] = matriz1[i][j] + matriz2[i][j]
    return matriz_suma

def restar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_resta = [[0] * columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matriz_resta[i][j] = matriz1[i][j] - matriz2[i][j]
    return matriz_resta

def main():
    print("Operaciones con matrices")
    
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    
    print("Ingrese la primera matriz:")
    matriz1 = leer_matriz(filas, columnas)
    if matriz1 is None:
        return

    print("Ingrese la segunda matriz:")
    matriz2 = leer_matriz(filas, columnas)
    if matriz2 is None:
        return

    print("\nPrimera matriz:")
    imprimir_matriz(matriz1)
    
    print("\nSegunda matriz:")
    imprimir_matriz(matriz2)
    
    print("\nSuma de matrices:")
    matriz_suma = sumar_matrices(matriz1, matriz2)
    imprimir_matriz(matriz_suma)
    
    print("\nResta de matrices:")
    matriz_resta = restar_matrices(matriz1, matriz2)
    imprimir_matriz(matriz_resta)

if __name__ == "__main__":
    main()
