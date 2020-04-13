from pytest import raises


def test__init_subclass__called_when_subclass_defined():
    class NoSubclass:
        __subclasses__ = []

        def __init_subclass__(cls):
            cls.__subclasses__.append(cls)

    class Superclass:
        __subclasses__ = []

        def __init_subclass__(cls):
            cls.__subclasses__.append(cls)

    assert Superclass.__subclasses__ == []

    class Subclass(Superclass):
        pass

    assert NoSubclass.__subclasses__ == []
    assert Superclass.__subclasses__ == [Subclass]


def test_raises_error_if_call_object__init_subclass__with_any_arguments():
    object.__subclasses__()

    with raises(TypeError, match=r"__subclasses__\(\) takes no arguments"):
        object.__subclasses__(int)
