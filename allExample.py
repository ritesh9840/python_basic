print(all([True, True, False]))
# All elements of list are true
l = [4, 5, 1]
print(all(l))

# All elements of list are false
l = [0, 0, False]
print(all(l))

# Some elements of list are
# true while others are false
l = [1, 0, 6, 7, False]
print(all(l))

# Empty List
l = []
print(all(l))

# all() with condition - to check if all elements are greater than 0
l = [1,-3,0,2,4]
print(all(ele > 0 for ele in l))


# All elements of tuple are true
t = (2, 4, 6)
print(all(t))

# All elements of tuple are false
t = (0, False, False)
print(all(t))

# Some elements of tuple
# are true while others are false
t = (5, 0, 3, 1, False)
print(all(t))

# Empty tuple
t = ()
print(all(t))

# all() with condition - to check if all elements are even
l = (2,4,6,8,10)
print(all(ele % 2 == 0 for ele in l))

# All elements of set are true
s = {1, 1, 3}
print(all(s))

# All elements of set are false
s = {0, 0, False}
print(all(s))

# Some elements of set
# are true while others are false
s = {1, 2, 0, 8, False}
print(all(s))

# Empty set
s = {}
print(all(s))

# all() with condition - to check if absolute of all elements is greater than 2
l = {-4, -3, 6, -5, 4}
print(all(abs(ele) > 2 for ele in l))

# All elements of dictionary are true
d = {1: "Hello", 2: "Hi"}
print(all(d))

# All elements of dictionary are false
d = {0: "Hello", False: "Hi"}
print(all(d))

# Some elements of dictionary
# are true while others are false
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(all(d))

# Empty dictionary
d = {}
print(all(d))

# all() with condition - to check if all letters of word 'time' are there
l = {"t": 1, "i": 1, "m": 2, "e": 0}
print(all(ele > 0 for ele in l.values()))

# Non-Empty String
s = "Hi There!"
print(all(s))

# Non-Empty String
s = "000"
print(all(s))

# Empty string
s = ""
print(all(s))