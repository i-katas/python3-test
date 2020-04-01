from pytest import fail


def test_assignment_expression():
    value = 'bar'  # assignment statement

    if bar := value:  # assignment expression
        assert value == bar and value == 'bar'
    else:
        fail()
