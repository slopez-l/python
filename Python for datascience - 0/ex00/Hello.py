ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Using index to modify the list; indexing starts at 0.
ft_list[1] = "World!"

# Convert a tuple into a list (to be able to change, add, or modify elements).
temp = list(ft_tuple)
temp[1] = "Euskadi!"
ft_tuple = tuple(temp)  # Converts a list to a tuple.

ft_set.discard("tutu!")  # .discard(value) removes it if present.
ft_set.add("Urduliz!")  # adds a new element to the set.

# Modifies the value associated with the key "Hello".
ft_dict["Hello"] = "42Urduliz!"
print(ft_list)
print(ft_tuple)
print(ft_set)  # returns a set with two elements, but with no guaranteed order.
print(ft_dict)
