"""70.escibe una funcion para clasificar si na sustancia
 es acida, basica o neutra apartir de su ph"""

def sustancia(ph):
	if ph < 7:
		return "acida"
	elif ph > 7:
		return "basica"
	else:
		return "neutra"

resulatdo = sustancia(7)

print(resulatdo)
