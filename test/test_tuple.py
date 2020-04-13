def test_create_empty_tuple():
    empty = ()

    assert type(empty) is tuple


def test_single_item_tuple():
    single = (3,)

    assert type(single) is tuple
    assert len(single) == 1
    assert single[0] == 3
