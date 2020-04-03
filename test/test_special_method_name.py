def test__delete__did_not_called_if_referenced_by_others():
    destroyed = []

    class Item:
        def __init__(self, id):
            self.id = id

        def __del__(self):
            destroyed.append(self.id)

    item1, item2 = Item(1), Item(2)
    refs = (item2)

    del item1, item2

    assert 1 in destroyed
    assert 2 not in destroyed

from . import mock_stderr

def test_exception_raised_in__delete__will_be_ignored_but_traceback_will_output_to_stderr():
    with mock_stderr() as stderr:
        class Item:
            def __del__(self):
                raise NotImplementedError()

        item = Item()

        del item
        assert 'NotImplementedError' in stderr.getvalue()

