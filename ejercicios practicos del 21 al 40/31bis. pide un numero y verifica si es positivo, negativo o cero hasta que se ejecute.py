"""31bis. pide un numero y verifica si es positivo, negativo o cero hasta que se ejecute"""

while True:
    entrada = input("Escribe un número: ")
    try:
        numero = int(entrada)
        break
    except ValueError:
        print("Eso no es un número válido. Inténtalo otra vez.")

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
