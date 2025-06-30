"""80.obtener la cantidad de memoria ram en mi computdora o laptop
pip install psutil"""

import psutil

def obtener_ram():
    memoria = psutil.virtual_memory()
    memoria_total = memoria.total / (1024 ** 3)#para conversion 
    return memoria_total

memoria = obtener_ram()

print("total ram ", memoria, "GB")
