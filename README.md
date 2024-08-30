# Reto-11

## Desarrolle la mayoría de ejercicios en clase, por cado punto resuelto en clase tendrá media décima en el examen 2 (créanme, las van a necesitar). Para cada punto cree un programa individual. Al finalizar suba todo a un repo y súbalo al canal reto_11 en slack.

### Punto 1 / Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```py
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
```
El programa primero pide al usuario que ingrese el tamaño de las matrices y luego cada una de sus filas. Utiliza funciones para leer la matriz, imprimirla y realizar las operaciones matemáticas. La función leer_matriz asegura que cada fila tenga el número correcto de columnas. La función imprimir_matriz muestra la matriz de manera clara. Las funciones sumar_matrices y restar_matrices realizan la suma y la resta de las matrices, respectivamente, y devuelven el resultado. Finalmente, la función main coordina el flujo del programa: solicita datos al usuario, realiza las operaciones y muestra los resultados.

### Punto 2 / Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```py
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
```

Este permite multiplicar dos matrices, siempre que las dimensiones sean compatibles para la operación. Primero, solicita al usuario las dimensiones de las dos matrices y luego los elementos de cada una. La función leer_matriz lee y valida cada fila para asegurar que tenga el número correcto de columnas. La función imprimir_matriz muestra las matrices en un formato legible. La función multiplicar_matrices realiza la multiplicación de las dos matrices si el número de columnas de la primera matriz es igual al número de filas de la segunda. Calcula el producto de las matrices y devuelve el resultado. Finalmente, la función main coordina el flujo del programa: recibe datos del usuario, realiza la multiplicación y muestra el resultado.

### Punto 3 / Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.


```py
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


```

Este programa  calcula la matriz transpuesta de una matriz dada. Primero, solicita al usuario las dimensiones de la matriz y luego los elementos de la misma. La función leer_matriz lee y valida cada fila de la matriz, asegurando que tenga el número correcto de columnas. La función imprimir_matriz muestra la matriz de manera clara. La función transponer_matriz realiza la transposición de la matriz, que implica intercambiar las filas y las columnas. Finalmente, la función main coordina el flujo del programa: recoge los datos del usuario, calcula la matriz transpuesta y muestra tanto la matriz original como la transpuesta.
### Punto 4 / Desarrollar un programa que sume los elementos de una columna dada de una matriz.
```py
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

```

permite sumar los elementos de una columna específica de una matriz. Primero, solicita al usuario las dimensiones de la matriz y luego los elementos de la misma. Usa funciones para leer la matriz (leer_matriz), imprimirla (imprimir_matriz), y calcular la suma de una columna (sumar_columna). La función leer_matriz valida que cada fila tenga el número correcto de columnas y maneja errores de entrada. La función imprimir_matriz muestra la matriz en un formato claro. La función sumar_columna suma los elementos de la columna indicada por el usuario, asegurándose de que el índice de columna sea válido. Finalmente, la función main coordina el flujo del programa, mostrando la matriz y el resultado de la suma.

### Punto 5 / Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```py
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

def sumar_fila(matriz, fila_index):
    """
    Suma los elementos de una fila específica.
    """
    if fila_index < 0 or fila_index >= len(matriz):
        print(f"Error: El índice de fila {fila_index} está fuera del rango.")
        return None
    
    suma = sum(matriz[fila_index])
    return suma

def main():
    print("Suma de elementos de una fila de una matriz")
    
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    
    print("Ingrese la matriz:")
    matriz = leer_matriz(filas, columnas)
    
    print("\nMatriz ingresada:")
    imprimir_matriz(matriz)
    
    while True:
        try:
            fila_index = int(input(f"\nIngrese el índice de la fila a sumar (0 a {filas - 1}): "))
            if 0 <= fila_index < filas:
                break
            else:
                print(f"Error: El índice debe estar entre 0 y {filas - 1}. Inténtalo de nuevo.")
        except ValueError:
            print("Error: Entrada inválida. Asegúrate de ingresar un número entero.")

    suma = sumar_fila(matriz, fila_index)
    if suma is not None:
        print(f"\nLa suma de los elementos de la fila {fila_index} es: {suma}")

if __name__ == "__main__":
    main()
```

Este programa suma los elementos de una fila específica en una matriz. Primero, solicita al usuario las dimensiones y los elementos de la matriz. La función leer_matriz lee y valida que cada fila tenga el número correcto de columnas, manejando posibles errores de entrada. La función imprimir_matriz muestra la matriz de manera clara. La función sumar_fila calcula la suma de los elementos de la fila seleccionada por el usuario, verificando que el índice de la fila sea válido. Finalmente, la función main coordina el flujo del programa, mostrando la matriz y el resultado de la suma.
