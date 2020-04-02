import numpy as np


def test_matrix_multiplication_by__matmul__operator():
    matrix = np.array([[1, 2, 3]]) @ np.array([[4, 7], [5, 8], [6, 9]])

    assert matrix.tolist() == [[4 + 2 * 5 + 3 * 6, 7 + 2 * 8 + 3 * 9]]


def test_power_numbers_by__pow__operator():
    assert 2 ** 3 == 8


def test_check_object_identity_by_is_operator():
    obj, other = [], []

    assert obj == other
    assert obj is obj and obj is not other
