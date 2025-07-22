number = int(input("Please type in a number: "))

for a in range(1, number + 1):
    for b in range(1, number + 1):
        print(f"{a} x {b} = {a * b}")
