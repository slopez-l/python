"""89.comprobar si una palabra es un plindromo usando lamba"""

palindromo = lambda palabra: palabra == palabra[::-1]

print(palindromo("radar")) #devuelve True
print(palindromo("hola"))
