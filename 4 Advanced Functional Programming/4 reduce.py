# reduce() - reduce given inputs into one value

from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))


# eg2
my_tuple = (1, 2, 3, 4, 5)


def reduce_example(a, b):
    print(a, b)
    return a + b


print(reduce(reduce_example, my_tuple))
