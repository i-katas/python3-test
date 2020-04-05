import sys
from pytest import raises

def test_set_class_metaclass():
    class MetaClass(type): 
        args = []
        def __init__(self, *args, **kwargs):
            self.args.extend(args)
            self.args.append(kwargs)
            super().__init__(args)

            
    class Base: 
        def __init_subclass__(cls, **kwargs):
            pass
    class Test(Base, metaclass=MetaClass, foo='bar'): pass

    args = MetaClass.args

    assert len(args) == 4   
    assert args[0] == 'Test'
    assert args[1] == (Base,)
    assert args[2] == dict(
        __module__=sys.modules[Test.__module__].__name__,
        __qualname__=Test.__qualname__
    )
    assert args[3] == dict(foo='bar')
    assert type(Test) is MetaClass


