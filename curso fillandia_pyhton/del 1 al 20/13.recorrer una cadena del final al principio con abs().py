string = input("Please type in a string:")

word = -1 #-1 es el ultimo caracter de la cadena, -2 penultimo
#abs()valor absoluto devuelve siempre valor positivo
while abs(word) <= len(string):
    print(string[word])
    word -= 1 #decrementa para recorreesla de final al principio

"""
Please type in a string: hiya
a
y
i
h
"""
