def function_creator():
    # expression to be evaluated
    expr = input("Enter the function(in terms of x):")

    # variable used in expression
    x = int(input("Enter the value of x:"))

    # evaluating expression
    y = eval(expr)

    # printing evaluated result
    print("y =", y)


if __name__ == "__main__":
    function_creator()

    '''
    output
    Enter the function(in terms of x):x+2-x*x
Enter the value of x:2
y = 0'''

    x = 5
    print(eval('x == 4'))

    x = None
    print(eval('x is None'))