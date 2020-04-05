def test_package__path__is_not_inherited():
    import sys
    
    paths = sys.modules[__package__].__path__

    assert 'foo' not in paths
