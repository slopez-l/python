def all_thing_is_obj(object: any) -> int:
    # Dictionary that maps common data types to more readable names
    type_names = {
        list: "List",        # lists like [1, 2, 3]
        tuple: "Tuple",      # tuples like (1, 2, 3)
        set: "Set",          # sets like {1, 2, 3}
        dict: "Dict",        # dictionaries like {"a": 1}
        str: "String"        # strings like "text"
    }

    # Get the actual type of the object passed as argument
    object_type = type(object)

    # Try to get a readable name for the type from the dictionary
    # If it's not in the dictionary, return the default message
    type_name = type_names.get(object_type, "Type not found")

    # If the object is a string, print a special message
    if object_type == str:
        print(f"{object} is in the kitchen : {object_type}")

    # If the type is in the dictionary,
    # print the custom name and the actual type
    elif type_name != "Type not found":
        print(f"{type_name} : {object_type}")

    # If the type was not in the dictionary,
    # print only the generic message
    else:
        print(f"{type_name}")

    # Always return the number 42, as required by the exercise
    return 42
