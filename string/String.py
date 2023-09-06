'''

The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step).

Syntax:

slice(stop)
slice(start, stop, step)
Parameters: start: Starting index where the slicing of object starts.
stop: Ending index where the slicing of object stops. step: It is an optional argument that determines the increment between each index for slicing.
Return Type: Returns a sliced object containing elements in the given range only.
'''


# Python program to demonstrate
# string slicing

# String slicing
String = 'ASTRING'

# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])