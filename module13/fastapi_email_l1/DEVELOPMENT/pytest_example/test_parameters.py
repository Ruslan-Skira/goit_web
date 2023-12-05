import pytest

@pytest.fixture
def add_f():
    return lambda x, y: x + y

# def add(f, s):
#     return f + s

# @pytest.mark.parametrize("first, second, result", [
#     (1, 2, 3),
#     ('hell', 'o', 'hello'),
#     (3, 4, 7)
# ])
# def test_add(add_f, first, second, result):
    assert add(first, second) == result

@pytest.mark.parametrize("first, second, result", [
    (1, 2, 3),
    ('hell', 'o', 'hello'),
    (3, 4, 7),
    (30, 40, 70)
])
def test_add(add_f, first, second, result):
    assert add_f(first, second) == result





