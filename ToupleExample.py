var = ("Geeks", "for", "Geeks")
print(var)


values = (1,2,4,"Geek")
print(values)

#Touple of one elelement

mytuple = ("Geeks",)
print(type(mytuple))

# NOT a tuple
mytuple = ("Geeks")
print(type(mytuple))


tuple_constructor = tuple(("dsa", "developement", "deep learning"))
print(tuple_constructor)


'''
What is Immutable in Tuples?
Tuples in Python are similar to Python lists but not entirely. Tuples are immutable and ordered and allow duplicate values. Some Characteristics of Tuples in Python.

We can find items in a tuple since finding any item does not make changes in the tuple.
One cannot add items to a tuple once it is created. 
Tuples cannot be appended or extended.
We cannot remove items from a tuple once it is created. 
Let us see this with an example.

'''

mytuple = (1, 2, 3, 4, 5)

# tuples are indexed
print(mytuple[1])
print(mytuple[4])

# tuples contain duplicate elements
mytuple = (1, 2, 3, 4, 2, 3)
print(mytuple)

# adding an element
mytuple[1] = 100
print(mytuple)

var = ("Geeks", "for", "Geeks")

print("Value in Var[0] = ", var[0])
print("Value in Var[1] = ", var[1])
print("Value in Var[2] = ", var[2])


'''
Access Tuple using Negative Index
In the above methods, we use the positive index to access the value in Python, and here we will use the negative index within [].

'''

var = (1, 2, 3)

print("Value in Var[-1] = ", var[-1])
print("Value in Var[-2] = ", var[-2])
print("Value in Var[-3] = ", var[-3])

# Code for concatenating 2 tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')

# Concatenating above two

print(tuple1 + tuple2)

# Code for creating nested tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')

tuple3 = (tuple1, tuple2)
print(tuple3)


# Code to create a tuple with repetition
tuple3 = ('python',)*3
print(tuple3)

'''
Slicing Tuples in Python
Slicing a Python tuple means dividing a tuple into small tuples using the indexing method.

'''

# code to test slicing
tuple1 = (0, 1, 2, 3)

print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])

'''
Output:

In this example, we sliced the tuple from index 1 to the last element. In the second print statement, 
we printed the tuple using reverse indexing. And in the third print statement, we printed the elements from index 2 to 4.
'''


#deleting is not allowd in  touple
# Code for deleting a tuple
tuple3 = (0, 1)

del tuple3
print(tuple3)


# Code for printing the length of a tuple
tuple2 = ('python', 'geek')
print(len(tuple2))


# tuple with different datatypes
tuple_obj = ("immutable",True,23)
print(tuple_obj)

# Code for converting a list and a string into a tuple
list1 = [0, 1, 2]

print(tuple(list1))

# string 'python'
print(tuple('python'))

# python code for creating tuples in a loop
tup = ('geek',)

# Number of time loop runs
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)