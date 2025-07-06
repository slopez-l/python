"""47.hacer un menu de opciones
 que incluye la opcion de salir de programa"""

while True:
    print("1 - suma")
    print("2 - restar")
    print("3 - salir")

    opcion = int(input("escribe tu opcion"))

    if opcion == 1:
        print("usted esta sumando")
    elif opcion == 2:
        print("usted esta restando")
    elif opcion == 3:
        break
    else:
        print("no es una opcion valida")

print("vuelve pronto")
