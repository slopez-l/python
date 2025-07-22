"""
escriba un programa para resolver una ecuación cuadrática de la
forma `ax²+bx+c`. El programa solicita los valores `a`, `b` y `c`.
 Luego, debe usar la fórmula cuadrática para resolver la ecuación.
   La fórmula cuadrática expresada con la función `sqrt` de Python
     es la siguiente:

x = (-b ± `sqrt(b²-4ac))/(2a)`.

Se puede asumir que la ecuación siempre tendrá dos raíces reales,
 por lo que la fórmula anterior siempre funcionará.

 An example of expected behaviour:

Sample output
Value of a: 1
Value of b: 2
Value of c: -8

The roots are 2.0 and -4.0
 """
from math import sqrt

# Ask for coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Compute the discriminant
discriminant = b**2 - 4*a*c

# Apply the quadratic formula
root1 = (-b + sqrt(discriminant)) / (2*a)
root2 = (-b - sqrt(discriminant)) / (2*a)

# Show results
print(f"The roots are: {root1:.1f} and {root2:.1f}")
