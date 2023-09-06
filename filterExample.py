# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)



'''
Filter Function in Python with Lambda
Python filter() function is normally used with Lambda functions. 
In this example, we are using the lambda function to filter out the odd and even numbers from a list.
'''

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


# Define a function to check
# if a number is a multiple of 3
def is_multiple_of_3(num):
    return num % 3 == 0


# Create a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter and a lambda function to
# filter the list of numbers and only
# keep the ones that are multiples of 3
result = list(filter(lambda x: is_multiple_of_3(x), numbers))

# Print the result
print(result)
