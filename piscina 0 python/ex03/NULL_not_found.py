import math

def NULL_not_found(obj: any) -> int:
	if obj is None:
		print("Nothing: None <class 'NoneType'>")
	elif isinstance(obj, float) and math.isnan(obj):
		print("Cheese: nan <class 'float'>")
	elif isinstance(obj, str) and obj == "":
		print("Empty: <class 'str'>")
	elif isinstance(obj, bool) and obj is False:
		print("Fake: False <class 'bool'>")
	elif isinstance(obj, int) and obj == 0:
		print("Zero: 0 <class 'int'>")
	else:
		print("Type not Found")
		return 1
	return 0
