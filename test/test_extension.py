import test.cmath as cmath


def test_extension_method():
    assert cmath.__doc__ == 'C math API'
    assert cmath.abs.__doc__ == 'absolute value of a number'
    assert cmath.abs(1) == 1
    assert cmath.abs(-1) == 1


def test_raises_exception_with_invalid_args():
    from pytest import raises
    with raises(TypeError, match=r'an integer is required \(got type str\)'):
        cmath.abs("bad")
