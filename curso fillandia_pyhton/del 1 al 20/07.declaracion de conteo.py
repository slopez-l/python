contador = 0

while True:
    number = int(input("Number:"))
    if number == 0:
        break
    contador += 1

print(f"Numbers typed in {contador}")

