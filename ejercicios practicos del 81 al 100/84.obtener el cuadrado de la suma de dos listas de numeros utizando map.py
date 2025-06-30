"""84.obtener el cuadrado
 de la suma de dos listas de numeros utizando map"""

def suma_cuadrados(a, b):
    return (a +b) ** 2

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

resultado = list(map(suma_cuadrados, lista1, lista2))

print(lista1)
print(lista2)
print(resultado)


