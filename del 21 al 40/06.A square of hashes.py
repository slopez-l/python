def line(longitud, simbolo):
    if simbolo == "":
        print("*" * longitud)
    else:
         print(simbolo[0] * longitud)


# Ahora la función 'square_of_hashes' que dibuja el cuadrado:
def square_of_hashes(longitud):
    i = 0
    while i < longitud:
        line(longitud, "#")  # Usamos la función 'line' para imprimir cada fila
        i += 1


if __name__ == "__main__":
    square_of_hashes(2)
