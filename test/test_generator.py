from collections.abc import Generator, Iterator, Iterable


def test_create_generator_comprehension():
    numbers = (n * 2 for n in [1, 2, 3])

    assert isinstance(numbers, Generator)
    assert isinstance(numbers, Iterator)
    assert isinstance(numbers, Iterable)


def test_generator_can_only_consumed_once():
    numbers = (n * 2 for n in [1, 2, 3])

    assert list(iter(numbers)) == [2, 4, 6]
    assert list(iter(numbers)) == []
