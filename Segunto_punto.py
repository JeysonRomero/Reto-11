def leer_matriz(filas, columnas):
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
    for fila in matriz:
        print(" ".join(map(str, fila)))

def multiplicar_matrices(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    
 
    if columnas1 != filas2:
        print("Error: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
        return None
    
   
    matriz_resultado = [[0] * columnas2 for _ in range(filas1)]
 
    for i in range(filas1):
        for j in range(columnas2):
            suma = 0
            for k in range(columnas1):
                suma += matriz1[i][k] * matriz2[k][j]
            matriz_resultado[i][j] = suma
    
    return matriz_resultado

def main():
    print("Multiplicación de matrices")
    
    filas1 = int(input("Ingrese el número de filas de la primera matriz: "))
    columnas1 = int(input("Ingrese el número de columnas de la primera matriz: "))
    filas2 = int(input("Ingrese el número de filas de la segunda matriz: "))
    columnas2 = int(input("Ingrese el número de columnas de la segunda matriz: "))
    
    print("Ingrese la primera matriz:")
    matriz1 = leer_matriz(filas1, columnas1)
    
    print("Ingrese la segunda matriz:")
    matriz2 = leer_matriz(filas2, columnas2)
    
    print("\nPrimera matriz:")
    imprimir_matriz(matriz1)
    
    print("\nSegunda matriz:")
    imprimir_matriz(matriz2)
    
    print("\nProducto de matrices:")
    matriz_producto = multiplicar_matrices(matriz1, matriz2)
    if matriz_producto:
        imprimir_matriz(matriz_producto)

if __name__ == "__main__":
    main()
