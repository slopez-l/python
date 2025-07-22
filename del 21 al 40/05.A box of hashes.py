# Función original solicitada
def line(longitud, simbolo):
    if simbolo == "":
        print("*" * longitud)
    else:
         print(simbolo[0] * longitud)

# Función nueva que usa la anterior
def box_of_hashes(altura):
    i = 0
    while i < altura:
        line(10, "#")  # Llamamos a line para imprimir 10 hashes
        i += 1


if __name__ == "__main__":
    box_of_hashes(4)

