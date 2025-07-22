word = input("Please type in a word:").strip().lower()
character = input("Please type in a character:").strip().lower()

index = word.find(character)

# Verificar si se encontró el carácter y si hay suficientes letras después
if index != -1 and index + 2 < len(word):
    print(word[index:index+3])
    #word.find(char)= devuelve el índice de la primera aparición del carácter.
    #  Si no lo encuentra, devuelve -1.
    #index + 2 < len(word)= verifica que hay al menos dos caracteres después del encontrado,
    #  para poder formar una subcadena de 3 letras.
    #Si se cumple todo, imprime word[index:index+3]

  # Este fragmento utiliza slicing (rebanado) para extraer una parte de la cadena word.

#index es la posición donde se encuentra por primera vez el carácter que el usuario eligió.

#index+3 indica el límite superior (no incluido) del corte.

#Entonces word[index:index+3] toma los tres caracteres que comienzan en index.
"""
salida:
Please type in a word: mammoth
Please type in a character: m
mam

Sample output
Please type in a word: banana
Please type in a character: n
nan

Sample output
Please type in a word: tomato
Please type in a character: x

Sample output
Please type in a word: python
Please type in a character: n
"""
