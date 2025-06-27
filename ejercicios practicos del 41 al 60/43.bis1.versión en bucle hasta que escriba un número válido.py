"""versión en bucle hasta que escriba un número válido"""

while True:
    entrada = input("Escribe un número: ")#Muestra el mensaje "Escribe un número: " al usuario y espera que escriba algo.
    try: #Inicia un bloque donde vas a intentar ejecutar código que podría fallar.
        numero = int(entrada)#si el numero no es valido salta a except
        print(f"✅ Ingresaste el número {numero}")
        break  # Salimos del bucle si va bien
    except ValueError:
	#Es una parte del control de errores en Python.
	#Se usa junto con try para atrapar errores (también llamados "excepciones")
    #Es un tipo específico de error que ocurre cuando intentas convertir un tipo de dato a otro y el contenido no tiene sentido.
        print("❌ Error: eso no es un número. Inténtalo otra vez.")
