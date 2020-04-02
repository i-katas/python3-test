def test_rewrite_class_private_names_into_mangled_form():
    class PrivateScopedName:
        def __init__(self, value):
            self.__value = value

    item = PrivateScopedName(3)
    qualifier = f'_{type(item).__name__}__value'

    assert not hasattr(item, '__value') \
           and hasattr(item, qualifier) \
           and getattr(item, qualifier) == 3


def test_class_use_system_names_not_to_be_rewritten():
    class SystemDefinedName:
        def __init__(self, value):
            self.__value__ = value

    assert hasattr(SystemDefinedName(3), '__value__')
