# Import the math module to use math.isnan().
import math


# Define a function that receives an object of any type and returns an integer.
def NULL_not_found(obj: any) -> int:

    # If the object is None (null value in Python).
    if obj is None:
        print("Nothing: None <class 'NoneType'>")

    # If the object is a floating-point number and also NaN (not a number).
    elif isinstance(obj, float) and math.isnan(obj):
        print("Cheese: nan <class 'float'>")

    # If the object is an empty string.
    elif isinstance(obj, str) and obj == "":
        print("Empty: <class 'str'>")

    # If the object is a boolean and the object is False.
    elif isinstance(obj, bool) and obj is False:
        print("Fake: False <class 'bool'>")

    # If the object is an integer equal to zero.
    elif isinstance(obj, int) and obj == 0:
        print("Zero: 0 <class 'int'>")

    else:
        print("Type not Found")
        return 1

    # Returns 0 if one of the cases was successfully detected and processed.
    return 0
