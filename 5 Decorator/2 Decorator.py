# Decorator - supercharges a function
# it wraps another function and enchances / charges it

def div(a, b):
    print(a/b)


d1 = div(10, 5)

d2 = div(5, 10)


def smartfun(fun):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return fun(a, b)
    return inner


# ztm eg
def my_decorator(fun):
    def wrapper_func():
        print('*' * 5)
        fun()
        print('*' * 5)
    return wrapper_func


@my_decorator
def hello():
    print('Helllooooo')


hello()


@my_decorator
def bye():
    print('See you later!')


bye()
