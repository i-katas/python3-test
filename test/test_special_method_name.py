from typing import SupportsInt

from pytest import raises

from . import mock_stderr


def test__del__did_not_called_if_referenced_by_others():
    """
    @ref https://docs.python.org/3/reference/datamodel.html#object.__del__
    """
    destroyed = []

    class Item:
        def __init__(self, id):
            self.id = id

        def __del__(self):
            destroyed.append(self.id)

    item1, item2 = Item(1), Item(2)
    refs = [item2]

    del item1, item2
    assert 1 in destroyed
    assert 2 not in destroyed

    refs.clear()
    assert destroyed == [1, 2]


def test_exception_raised_in__del__will_be_ignored_but_traceback_will_output_to_stderr():
    """
    @ref https://docs.python.org/3/reference/datamodel.html#object.__del__
    """
    with mock_stderr() as stderr:
        class Item:
            def __del__(self):
                raise NotImplementedError()

        item = Item()

        del item
        assert 'NotImplementedError' in stderr.getvalue()


def test__le__operator():
    """
    @ref https://docs.python.org/3/reference/datamodel.html#object.__lt__
    """

    class Count:
        def __init__(self, value=0):
            self._value = value

        def __le__(self, other):
            return self._value <= other._value

    assert Count(value=1) <= Count(value=2) <= Count(value=2)


def test__int__like_objects():
    """
    @ref https://docs.python.org/3/reference/datamodel.html#object.__int__
    """

    class Count():
        def __init__(self, value=0):
            self._value = value

        def __int__(self):
            return self._value

    assert isinstance(Count(), SupportsInt)
    assert int(Count(2)) == 2


def test_disable_hash_by_set__hash__to_None():
    """
    @ref https://docs.python.org/3/reference/datamodel.html#object.__hash__
    """

    class Unhashable:
        __hash__ = None

    with raises(TypeError, match="unhashable type: 'Unhashable'"):
        hash(Unhashable())


def test_str_and_bytes_hash_take_a_random_salt_per_processor():
    """
    @ref https://docs.python.org/3/reference/datamodel.html#object.__hash__
    """
    import sys
    import subprocess

    def proc_hash(s):
        command = f'{sys.executable} -c "print(hash({repr(s)}))"'
        return int(subprocess.check_output(command, shell=True))

    assert hash('foo') == hash('foo')
    assert hash('foo') != proc_hash('foo')
    assert hash(b'foo') == hash(b'foo')
    assert hash(b'foo') != proc_hash(b'foo')


def test__getattribute__will_be_bypassed_with_implicit_special_method_lookup():
    """
    @ref https://docs.python.org/3/reference/datamodel.html#special-lookup
    """
    visited = []

    class Context:
        def __getattribute__(self, name: str):
            visited.append((self, name))
            return object.__getattribute__(self, name)

    context = Context()

    assert context.__str__() and visited[:] == [(context, '__str__')]

    del visited[:]
    assert str(context) and not visited
