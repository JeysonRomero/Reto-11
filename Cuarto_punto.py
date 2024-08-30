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

def sumar_columna(matriz, columna_index):
    """
    Suma los elementos de la columna especificada.
    """
    filas = len(matriz)
    suma = 0
    for i in range(filas):
        if columna_index < len(matriz[i]):
            suma += matriz[i][columna_index]
        else:
            print(f"Error: El índice de columna {columna_index} está fuera del rango.")
            return None
    return suma

def main():
    print("Suma de elementos de una columna de una matriz")
    
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    
    print("Ingrese la matriz:")
    matriz = leer_matriz(filas, columnas)
    
    print("\nMatriz ingresada:")
    imprimir_matriz(matriz)
    
    while True:
        try:
            columna_index = int(input(f"\nIngrese el índice de la columna a sumar (0 a {columnas - 1}): "))
            if 0 <= columna_index < columnas:
                break
            else:
                print(f"Error: El índice debe estar entre 0 y {columnas - 1}. Inténtalo de nuevo.")
        except ValueError:
            print("Error: Entrada inválida. Asegúrate de ingresar un número entero.")

    suma = sumar_columna(matriz, columna_index)
    if suma is not None:
        print(f"\nLa suma de los elementos de la columna {columna_index} es: {suma}")

if __name__ == "__main__":
    main()
