from typing import List

__ANNOTATIONS__, __DEFAULTS__, __KWDEFAULTS__ = '__annotations__', '__defaults__', '__kwdefaults__'


def test_func_metadata():
    def empty():
        pass

    assert empty.__name__ == 'empty'
    assert empty.__module__ == 'test.test_func_metadata'
    assert hasattr(empty, __KWDEFAULTS__)


def test_func_with_params_types_has_empty_annotations():
    def no_params():
        pass

    def params_missing_type(_):
        pass

    assert not getattr(no_params, __ANNOTATIONS__)
    assert not getattr(no_params, __DEFAULTS__)
    assert not getattr(params_missing_type, __ANNOTATIONS__)


def test_func_with_params_and_params_type_has_annotations():
    def params_with_type(_: int) -> List[int]:
        pass

    assert not getattr(params_with_type, __DEFAULTS__)
    assert getattr(params_with_type, __ANNOTATIONS__) == {'_': int, 'return': List[int]}


def test_func_with_default_value():
    def params_with_defaults(_=[]):
        pass

    assert getattr(params_with_defaults, __KWDEFAULTS__) is None
    assert getattr(params_with_defaults, __DEFAULTS__) == ([],)
    assert not getattr(params_with_defaults, __ANNOTATIONS__)


def test_func_with_kwargs():
    def keyword_params(**kwargs):
        pass

    assert getattr(keyword_params, __KWDEFAULTS__) is None
    assert not getattr(keyword_params, __ANNOTATIONS__)
