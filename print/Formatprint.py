'''
Formatting Output using String Modulo Operator(%)
The Modulo % operator can also be used for string formatting.
It interprets the left argument much like a printf()-style format as in C language strings to be applied to the right argument.
In Python, there is no printf() function but the functionality of the ancient printf is contained in Python.
To this purpose, the modulo operator % is overloaded by the string class to perform string formatting. Therefore,
it is often called a string modulo (or sometimes even called modulus) operator.
The string modulo operator ( % ) is still available in Python(3.x) and is widely used. But nowadays the old style of formatting is removed from the language.

'''
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))

print("Total students : %3d, Boys : %2d" % (240, 120))  # print integer value

print("%7.3o" % (25))  # print octal value

print("%10.3E" % (356.08977))  # print exponential value

print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# using format() method and referring a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))

print('{1} and {0}'.format('Geeks', 'Portal'))

print(f"I love {'Geeks'} for \"{'Geeks'}!\"")

# using format() method and referring a position of the object
print(f"{'Geeks'} and {'Portal'}")

# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
      .format('Geeks', 'For', other='Geeks'))

# using format() method with number
print("Geeks :{0:2d}, Portal :{1:8.2f}".
      format(12, 00.546))

# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
      format(47.42, 11))

print("Geeks: {a:5d},  Portal: {p:8.2f}".
      format(a=453, p=59.058))

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}

# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
      'Geeks: {0[geek]:d}'.format(tab))

data = dict(fun="GeeksForGeeks", adj="Portal")

print("I love {fun} computer {adj}".format(**data))

cstr = "I love geeksforgeeks"

# Printing the center aligned string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))

# Printing the left aligned string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))





'''
Python’s Format Conversion Rule
This table lists the standard format conversion guidelines used by Python’s format() function.

Conversion

Meaning

d

Decimal integer

b

Binary format

o

octal format

u

Obsolete and equivalent to ‘d’

x or X

Hexadecimal format

e or E

Exponential notation

f or F

Floating-point decimal

g or G

General format

c

Single Character

r

String format(using repr())

s

String Format(using str()))

%

Percentage
'''