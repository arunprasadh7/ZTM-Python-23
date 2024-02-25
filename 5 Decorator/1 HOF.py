# Higher order functions HOF
# a function which accepts another function as an argument or returns another function is called HOF

# def greet(fun):
#     fun()


# def greeet():
#     def func():
#         return 5
#     return func


# Decorators Basics
def hello(fun):
    fun()


def welcome():
    print('This is Sparta!!')


a = welcome
hello(a)
