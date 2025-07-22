frase = input("Please type in a sentence: ")

# Dividir la frase en palabras
palabras = frase.split()

# Recorremos la lista manualmente con un índice
i = 0
while i < len(palabras):
    print(palabras[i][0])
    i += 1
