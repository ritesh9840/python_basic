main_dict = {'a': 1, 'b': 2, 'c': 3}

# deep copy using dict
dict_deep = dict(main_dict)

# shallow copy without dict
dict_shallow = main_dict

# changing value in shallow copy will change main_dict
dict_shallow['a'] = 10
print("After change in shallow copy, main_dict:", main_dict)

# changing value in deep copy won't affect main_dict
dict_deep['b'] = 20
print("After change in deep copy, main_dict:", main_dict)

# A list of key value pairs is passed and
# a keyword argument is also passed
myDict = dict([('a', 1), ('b', 2), ('c', 3)], d=4)

print(myDict)