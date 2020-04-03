def test_function_defaults_is_shared_globally():
    def dangerous(array: list = []) -> list:
        array.append(1)
        return array

    result = dangerous()

    assert dangerous() == result
    assert result == [1, 1]


def test_transformation_from_function_object_to_instance_method_object_happens_each_time_when_retrieve_from_the_instance_except_user_defined_functions():
    class Methods:
        def test(self, arg:int = None, *args): pass

    methods = Methods()
    methods.after = lambda: None

    assert methods.test.__self__ is methods
    assert methods.test is not methods.test
    assert methods.after is methods.after
