from pytest import raises


def test_getter():
    item = Item(qty=3)

    assert item.qty == 3


def test_setter():
    item = Item(qty=3)

    item.qty = 4

    assert item.qty == 4 and item._qty == item.qty


def test_delete():
    item = Item(qty=3)
    assert '_qty' in dir(item)

    del item.qty

    assert '_qty' not in dir(item)


def test_get_value_from_none_object():
    assert Item.qty.__get__(None, Item) == Item.qty
    with raises(TypeError, match=r'__get__\(None, None\) is invalid'):
        Item.qty.__get__(None, None)


def test_set_value_into_none_object():
    with raises(AttributeError, match=r"'NoneType' object has no attribute '_qty'"):
        Item.qty.__set__(None, None)


def test_delete_on_none_object():
    with raises(AttributeError, match=r"'NoneType' object has no attribute '_qty'"):
        Item.qty.__delete__(None)


def test_raise_error_when_set_value_on_readonly_property():
    item = Item(name='iPhone')

    assert item.name == 'iPhone'

    with raises(AttributeError, match='`name` is readonly'):
        item.name = 'Mi3'


class PropertyDescriptor:
    def __init__(self, getter=None, setter=None, deleter=None):
        self.__getter__, self.__setter__, self.__deleter__ = getter, setter, deleter

    def __get__(self, obj=None, objtype=None):
        if obj is None and objtype is None:
            raise TypeError('__get__(None, None) is invalid')
        return self.__getter__(obj) if obj is not None else self

    def __set__(self, obj, value):
        if self.__setter__ is None:
            raise AttributeError(f'`{self.__getter__.__name__}` is readonly')
        return self.__setter__(obj, value)

    def __delete__(self, obj):
        return self.__deleter__(obj)

    def setter(self, setter):
        return type(self)(self.__getter__, setter, self.__deleter__)

    def deleter(self, deleter):
        return type(self)(self.__getter__, self.__setter__, deleter)


def property(getter, setter=None, deleter=None):
    return PropertyDescriptor(getter, setter, deleter)


class Item:
    def __init__(self, name: str = None, qty: int = 0):
        self._name, self._qty = name, qty

    @property
    def qty(self):
        return self._qty

    @qty.deleter
    def qty(self):
        del self._qty

    @qty.setter
    def qty(self, qty):
        self._qty = qty

    @property
    def name(self):
        return self._name
