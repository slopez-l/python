# Definimos una función llamada chessboard que recibe el tamaño del tablero como argumento
def chessboard(casilla):

    fila = 0  # Esta variable indica en qué fila estamos, empieza en 0

    # Este bucle se repite una vez por cada fila del tablero
    while fila < casilla:

        columna = 0  # Reiniciamos la columna cada vez que empieza una nueva fila

        # Este bucle construye cada fila, repitiéndose tantas veces como columnas haya
        while columna < casilla:

            # Usamos la suma de los índices para alternar entre 1 y 0 en forma de tablero
            if (fila + columna) % 2 == 0:
                print("1", end="")  # Si la suma es par, imprimimos un "1" sin salto de línea
            else:
                print("0", end="")  # Si la suma es impar, imprimimos un "0" sin salto de línea

            columna += 1  # Pasamos a la siguiente columna

        print()  # Cuando termina la fila, añadimos un salto de línea para empezar la siguiente
        fila += 1  # Pasamos a la siguiente fila

# Este bloque se ejecuta solo si el programa se corre directamente (no al importarse como módulo)
if __name__ == "__main__":
    chessboard(3)  # Llamamos a la función para imprimir un tablero de 3x3

"""
salida:
101
010
101
"""
