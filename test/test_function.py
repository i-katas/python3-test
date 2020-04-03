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


def empty(): pass
def one(_): pass
def kwargs(**_): pass
def args(*_): pass
def generator(): yield 
async def asynchronous(): pass
function = type(empty)

def test_arguments_flags():
    def flags_of(fun: function): return fun.__code__.co_flags
    def assert_flags_of(func, flags, message):
        assert (diff := flags_of(empty) ^ flags_of(func)) == flags_of(func) & flags == flags, (flags_of(empty), flags_of(func), flags, message)

    assert type(flags_of) is function
    assert_flags_of(args, 0x04, 'arbitray args flags') 
    assert_flags_of(kwargs, 0x08, 'keyword arguments flags') 
    assert_flags_of(generator, 0x20, 'generator function flags') 
    assert_flags_of(asynchronous, 0x80, 'arbitray args flags') 
    assert_flags_of(flags_of, 0x10, 'nested scope function flags') 
    

