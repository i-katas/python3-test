def test_function_defaults_is_shared_globally():
    def dangerous(array: list = []) -> list:
        array.append(1)
        return array

    result = dangerous()
    
    assert dangerous() == result
    assert result == [1, 1]
