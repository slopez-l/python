def squared(s, n):
    # Guardamos la longitud del string para usar en cálculo circular.
    length = len(s)

    # Función recursiva que construye una línea (fila) del cuadrado.
    def build_line(start, j=0, line=""):
        if j == n:
            # Caso base: si ya hemos añadido n caracteres, devolvemos la línea completa
            return line
        index = (start + j) % length  # Índice circular para recorrer el string
        # Llamada recursiva añadiendo el siguiente carácter a la línea
        return build_line(start, j + 1, line + s[index])

    # Función recursiva que imprime cada línea del cuadrado
    def build_square(start, i=0):
        if i == n:
            # Caso base: si ya imprimimos n líneas, terminamos la recursión
            return
        print(build_line(start))  # Construimos e imprimimos la línea actual
        # Llamada recursiva para imprimir la siguiente línea
        # La siguiente línea empieza donde terminó la anterior (avanzamos n posiciones)
        build_square((start + n) % length, i + 1)

    # Inicio del proceso, empezamos desde índice 0 y línea 0
    build_square(0)

# Prueba
if __name__ == "__main__":
    squared("aybabtu", 5)

