import time
from functools import wraps

"""
Показати декорування з wraps та без нього. Without the use of this decorator factory, the name of the example function would have been 'wrapper', and the docstring of the original example() would have been lost.
"""


def wrong_timelogger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start}")
        return result

    return wrapper


def timelogger(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"{func.__name__}: {end - start}")
        return result

    return wrapper



# @wrong_timelogger
@timelogger
def long_loop(num: int) -> None:
    """
    Long loop function

    :param num:
    :return: None
    """

    while num > 0:
        num -= 1



if __name__ == "__main__":
    long_loop(100_000)
    # hello()
    print(f"Function name: {long_loop.__name__}")
    print(f"Docstring function: {long_loop.__doc__}")
    print(f"Annotation function: {long_loop.__annotations__}")
