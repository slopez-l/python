def squared(s, n):
    length = len(s)
    start = 0  # Índice inicial para cada línea

    for _ in range(n):  # Generar n filas
        row = ""
        for j in range(n):  # Cada fila tiene n caracteres
            index = (start + j) % length  # Índice circular
            row += s[index]
        print(row)
        start = (start + n) % length  # Avanzamos al siguiente punto de partida



# Prueba
if __name__ == "__main__":
    squared("123456789", 100)
