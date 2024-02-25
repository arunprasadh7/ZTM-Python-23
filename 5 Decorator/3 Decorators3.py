# Decorators 3

def outer(fun):
    def wrapper_fun(name):
        print('*****')
        fun(name)
        print('*****')

    return wrapper_fun


@outer
def hello(name):
    print(f'Hello {name}')


hello('Arun')


# Decorator pattern using *args **kwargs

def my_decorator(fun):
    def wrapper(*args, **kwargs):
        print('**********')
        fun(*args, **kwargs)
        print('**********')

    return wrapper


@my_decorator
def greet(greet, emoji=':)'):
    print(greet, emoji)


greet('Hello')
greet('Future IAS of TamilNadu', 'XD')
