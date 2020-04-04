def test_saves_all_attributes_in__dict__():
    class Type:
        a:int = 1

    assert Type.__annotations__ == {'a': int}
    assert Type.a == 1 and Type.a == Type.__dict__['a']

def test_get_object_attrs_from__dict__and_then_class__dict__():
    class Class:
        a:int = 1
        b:int = 2
        def __init__(self):
            self.b, self.c = 3, 4

    obj = Class()

    assert obj.c == 4 and obj.c == obj.__dict__['c'] and 'c' not in Class.__dict__
    assert obj.b == 3 and obj.b == obj.__dict__['b'] and Class.b == 2
    assert obj.a == 1 and obj.a == Class.a and 'a' not in obj.__dict__


class NonDataDescriptor:
    def __init__(self, *args): pass
    def __get__(self, obj, obj_t): return 1

def test_attr_access_overrided_by_descriptor_but_can_be_access_direct_by__dict__():
    class Class:
        @NonDataDescriptor
        def value(): pass

    obj = Class()

    assert type(Class.__dict__['value']) is NonDataDescriptor 
    assert Class.value == 1 and Class.value is obj.value


def test_non_data_descriptor_overrieded_by_instance__dict__():
    class Class:
        @NonDataDescriptor
        def value(): pass

    obj = Class()

    obj.__dict__['value'] = 2 # equivalent to obj.value = 2

    assert Class.value == 1 and obj.value == 2


def test_data_descriptor_can_not_be_overrieded_by_instance__dict__():
    class DataDescriptor(NonDataDescriptor):
        def __set__(*args): pass

    class Class:
        @DataDescriptor
        def value(): pass

    obj = Class()

    obj.__dict__['value'] = 2 # equivalent to obj.value = 2

    assert Class.value == 1 and obj.value == Class.value


