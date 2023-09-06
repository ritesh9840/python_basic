'''
Method 1: Using the slice() method
The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step).

Syntax:

slice(stop)
slice(start, stop, step)
Parameters: start: Starting index where the slicing of object starts.
stop: Ending index where the slicing of object stops. step:
It is an optional argument that determines the increment between each index for slicing. Return Type:
Returns a sliced object containing elements in the given range only.


'''

# Python program to demonstrate
# string slicing

# String slicing
String = 'ASTRING'

# Using slice constructor
s1 = slice(3) #for positive index start from 0
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)   #for negative index start from -1

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])

# Python program to demonstrate
# string slicing

# String slicing
String = 'GEEKSFORGEEKS'

# Using indexing sequence
print(String[:3])

# Python program to demonstrate
# string slicing

# String slicing
String = 'GEEKSFORGEEKS'

# Using indexing sequence
print(String[1:5:2])

# Python program to demonstrate
# string slicing

# String slicing
String = 'GEEKSFORGEEKS'

# Using indexing sequence
print(String[-1:-12:-2])

# Python program to demonstrate
# string slicing

# String slicing
String = 'GEEKSFORGEEKS'

# Prints string in reverse
print(String[::-1])  #rever string

# Python program to demonstrate
# islice()

import itertools

# Using islice()
String = 'GEEKSFORGEEKS'

# prints characters from 3 to 7 skipping one character.
print(''.join(itertools.islice(String, 3, 7)))
# This code is contributed by Edula Vinay Kumar Reddy


import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print('Start')