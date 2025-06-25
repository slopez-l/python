"""17bis. extrae una subcadena de una cadena dada, usando find()"""

frase = "Hola, me llamo Sergio"
inicio = frase.find("o")
fin = frase.find("S")
sub = frase[inicio:fin].strip()
print(sub)  # ola, me llamo
