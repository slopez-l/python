n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)#espacios para centrar la estrella
    row += "**"#incrmenta en cada interaccion
    n -= 1#desminulle espacio a la vez que se incrementa la estralla
