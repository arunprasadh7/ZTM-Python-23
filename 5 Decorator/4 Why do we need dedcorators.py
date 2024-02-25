# Why do we need decorators

from time import time


def check_time(fun):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fun(*args, **kwargs)
        t2 = time()
        print(f'Took {t2-t1} seconds to complete.')
        return result

    return wrapper


@check_time
def time_taken():
    for i in range(10000000):
        i * 5


time_taken()
