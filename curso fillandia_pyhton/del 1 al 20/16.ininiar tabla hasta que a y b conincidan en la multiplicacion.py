number = int(input("Please type in a number: "))

a = 1
while a <= number:
    b = 1
    while b <= number:
        print(f"{a} x {b} = {a * b}")
        b += 1
    a += 1

"""
salida:
Please type in a number: 3
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
"""
