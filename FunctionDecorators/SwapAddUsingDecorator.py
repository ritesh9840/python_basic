
def new_div(func):
    def inner(a ,b):
        if a< b:a, b = b, a
        return func(a, b)
    return inner


@new_div
def div(a, b):
    print(a / b)


# calling function as decorator
div(2, 5)
