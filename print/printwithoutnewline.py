# Python 3 code for printing
# on the same line printing
# geeks and geeksforgeeks
# in the same line

print("geeks", end=" ")
print("geeksforgeeks")

# array
a = [1, 2, 3, 4]

# printing a element in same
# line
for i in range(4):
    print(a[i], end=" ")

# Print without newline in Python 3.x without using for loop

l = [1, 2, 3, 4, 5, 6]

# using * symbol prints the list
# elements in a single line
print(*l)

import sys

sys.stdout.write("GeeksforGeeks ")
sys.stdout.write("is best website for coding!")