def all_thing_is_obj(obj: any) -> int:
    if type(obj) == list:
        print("List : <class 'list'>")
    elif type(obj) == tuple:
        print("Tuple : <class 'tuple'>")
    elif type(obj) == set:
        print("Set : <class 'set'>")
    elif type(obj) == dict:
        print("Dict : <class 'dict'>")
    elif isinstance(obj, str):
        if obj == "Brian":
            print("Brian is in the kitchen : <class 'str'>")
        elif obj == "Toto":
            print("Toto is in the kitchen : <class 'str'>")
        else:
            print(f"Unknown string : {type(obj)}")
    else:
        print("Type not found")
    return 42
