'''
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.) Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable. iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function. Returns :

Returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)
  NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set)

'''




# of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print("print lst using lambda",list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print('print two list',list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


# Define a function that doubles even numbers and leaves odd numbers as is
def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


# Create a list of numbers to apply the function to
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
result = list(map(double_even, numbers))

# Print the result
print(result)  # [1, 4, 3, 8, 5]

