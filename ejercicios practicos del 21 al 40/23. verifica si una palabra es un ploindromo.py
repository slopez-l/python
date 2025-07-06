"""23. verifica si una palabra es un ploindromo
palabra o frase que se lee igual de de izquierda
a de deracha que decha a izquierda"""

palabra = "radar444"  # sin los 444 sale True

es_pa = palabra == palabra[::-1]

print("es polindromo ", es_pa)
