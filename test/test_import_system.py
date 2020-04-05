def test_imported_module_cached():
    from importlib import import_module

    module = import_module('sys', 'sys')
    import sys

    assert sys is module

def test_package__path__():
    import sys

    package = sys.modules[__package__]

    assert 'foo' in package.__path__

