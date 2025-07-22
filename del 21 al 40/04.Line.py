def line(longitud, simbolo):
    if simbolo == "":
        print("*" * longitud)
    else:
         print(simbolo[0] * longitud)

if __name__ == "__main__":
    line(7, "LOJ")

