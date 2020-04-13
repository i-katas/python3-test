from pytest import raises


def test_reject_unlisted_attribute_assignment():
    """
    @ref https://docs.python.org/3/reference/datamodel.html#slots
    """

    slot = Slot()
    assert 'name' in dir(slot)

    slot.name = 'test'
    assert slot.name == 'test'

    with raises(AttributeError):
        slot.other = 'failed'


def test_slot_and_builtin_object_without__dict__():
    class Custom:
        pass

    slot, custom_obj, builtins_obj = Slot(), Custom(), object()

    assert not hasattr(slot, '__dict__')
    assert not hasattr(builtins_obj, '__dict__')
    assert hasattr(custom_obj, '__dict__')


def test_multiple_inheritance_allows_one_superclass_has_attributes__slots__():
    class A:
        __slots__ = 'a'

    class B:
        __slots__ = 'b'

    class C:
        pass

    class Satisfied(A, C):
        pass

    with raises(TypeError, match='multiple bases have instance lay-out conflict'):
        class Conflicted(A, B):
            pass


def test_parent__slots__available_to_subclass_but_subclass_also_have__dict__unless_they_also_defines__slots__():
    class Subclass(Slot):
        pass

    obj = Subclass()

    assert obj.__slots__ is Slot.__slots__
    assert hasattr(obj, '__dict__')


def test__class__assignment_works_only_if_both_class_have_the_same__slots():
    class Compatible:
        __slots__ = Slot.__slots__

    class Incompatible:
        __slots__ = 'diff'

    slot = Slot()
    slot.__class__ = Compatible

    slot = Slot()
    with raises(TypeError, match='object layout differs'):
        slot.__class__ = Incompatible


class Slot:
    __slots__ = 'name'
