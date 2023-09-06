'''
A Set in Python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements.

Set are represented by { } (values enclosed in curly braces)

The major advantage of using a set, as opposed to a list,
 is that it has a highly optimized method for checking whether
 a specific element is contained in the set. This is based on a data structure known as a hash table.
 Since sets are unordered, we cannot access items using indexes as we do in lists.
'''


var = {"Geeks", "for", "Geeks"}
print(type(var))

# typecasting list to set
myset = set(["a", "b", "c"])
print(myset)

# Adding element to the set
myset.add("d")
print(myset)

# Python program to demonstrate that
# a set cannot have duplicate values
# and we cannot change its items

# a set cannot have duplicate values
myset = {"Geeks", "for", "Geeks"}
print(myset)

# values of a set cannot be changed
myset[1] = "Hello"
print(myset)



# Python example demonstrate that a set
# can store heterogeneous elements
myset = {"Geeks", "for", 10, 52.7, True}
print(myset)

# Python program to demonstrate differences
# between normal and frozen set

# Same as {"a", "b","c"}
normal_set = set(["a", "b", "c"])

print("Normal Set")
print(normal_set)

# A frozen set
frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(frozen_set)

# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# frozen_set.add("h")


'''
Methods for Sets
Adding elements to Python Sets
Insertion in the set is done through the set.add() 
function, where an appropriate record value is created to store in the hash table. 
Same as checking for an item, i.e., O(1) on average. However, in worst case it can become O(n).
'''

# A Python program to
# demonstrate adding elements
# in a set

# Creating a Set
people = {"Jay", "Idrish", "Archi"}

print("People:", end=" ")
print(people)

# This will add Daxit
# in the set
people.add("Daxit")

# Adding elements to the
# set using iterator
for i in range(1, 6):
    people.add(i)

print("\nSet after adding element:", end=" ")
print(people)