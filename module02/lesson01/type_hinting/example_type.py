from typing import List, Union, TypeVar, Any

Number = int | float  # Union[float, int]  #
"""Універсальні обʼєкти можна параметризувати за допомогою фабрики, доступної в наборі під назвою TypeVar."""
T = TypeVar("T", int, str, float, list)  # https://docs.python.org/3.9/library/typing.html?highlight=typehinting#typing.TypeVar

def calculator(x: T, y: T) -> T:
    return x + y


def my_mul(data: List[Number]) -> float:
    result = 1.0
    for num in data:
        result = result * num
    return result

"""Використовуйте Any, щоб вказати, що значення вводиться динамічно"""

from typing import Any

a: Any = None
a = []          # OK
a = 2           # OK

s: str = ''
s = a           # OK

def foo(item: Any) -> int:
    # Typechecks; 'item' could be any type,
    # and that type might have a 'bar' method
    item.bar()
    ...

if __name__ == "__main__":
    r = my_mul([2, 3, 4.5])
    print(r)
    print(calculator(3, 5))
    print(calculator("Hello", "World"))
    print(calculator(3.5, 4))
    print(calculator([2, 3, 4.5], [2, 3, 4.5]))
