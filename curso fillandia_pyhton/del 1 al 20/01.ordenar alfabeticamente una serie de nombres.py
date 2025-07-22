"""Se supone que este programa imprime los nombres
de los hermanos en orden alfabético, pero aún no
funciona correctamente. Por favor, arreglen el
 programa para que los nombres se impriman
 correctamente."""

brothers = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
brothers.sort()

for name in brothers:
    print(name)

"""salida:
Aapo
Eero
Juhani
Lauri
Simeoni
Timo
Tuomas
"""
