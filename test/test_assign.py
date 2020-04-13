from pytest import fail


def test_assignment_expression():
    value = 'bar'  # assignment statement

    if bar := value:  # noqa: E701, E231
        assert value == bar and value == 'bar'
    else:
        fail()
