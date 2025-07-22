string = input("Please type in a string:")

word = -1 #-1 es el ultimo caracter de la cadena, -2 penultimo
while abs(word) < len(string):#abs()valor absoluto devuelve siempre valor positivo
    print(string[word])
    word -= 1 #decrementa para recorreesla de final al principio

"""
Please type in a string: hiya
a
y
i
h
"""
