import inspect
from typing import Iterator


def test_generator():
    seq = (n for n in [])
    assert inspect.isgenerator(seq) and isinstance(seq, Iterator)


def test_find_first_matched_value():
    numbers = [1, 2, 3, 4]

    assert next(n for n in numbers if n % 2 == 0) == 2
    assert next((n for n in numbers if n > 5), None) is None
