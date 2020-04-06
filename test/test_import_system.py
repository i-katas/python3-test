def test_imported_module_cached():
    from importlib import import_module

    module = import_module('sys', 'sys')
    import sys

    assert sys is module


def test_package__path__():
    import sys

    package = sys.modules[__package__]

    assert 'foo' in package.__path__


def test_import_namespace_packages():
    import sys
    sys.path.extend(namespace_paths())

    from lib import name, version

    assert name.value == 'namespace package'
    assert version.value == '1.0'


def test_import_namespace_packages_for_package():
    import sys

    sys.modules[__package__].__path__.extend(namespace_paths())

    from .lib import name, version

    assert name.value == 'namespace package'
    assert version.value == '1.0'

from typing import Generator, Iterator
def namespace_paths() -> Generator[str, None, None]:
    import sys
    from os import path
    namespaces = ['version1', 'version2']
    parent_path = path.dirname(__file__)
    return (path.join(parent_path, 'fixtures', name) for name in namespaces)


def test_modules_contain_packages_and_file_modules():
    import sys

    assert sys.modules[__package__] and sys.modules[__name__]


def test_package_loaded_when_import_module_from_it():
    from sys import modules
    from .fixtures import stub
    
    assert modules[stub.__package__] and modules[stub.__name__]


def test_find_entry_path_from_path_hooks():
    from pytest import raises
    import sys, importlib

    repo = 'http://example.com/libs'
    searched = []
    def find_path_entry_finder(path):
        searched.append(path)
        raise ImportError("No service")
    sys.path.append(repo)
    sys.path_hooks.append(find_path_entry_finder)

    assert not searched
    assert repo not in sys.path_importer_cache, f'finder for {repr(repo)} is cached'
    with raises(ImportError):
        import fib

    assert searched == [repo]
    assert repo in sys.path_importer_cache, f'finder for {repr(repo)} is not cached'
    assert sys.path_importer_cache[repo] is None

