"""Test Complexity module"""


from lib.complexity_m import per_missing_element


def test_c_1():
    A = [2, 3, 1, 5]
    assert per_missing_element(A) == 4


def test_c_2():
    A = [2, 3, 4, 5]
    assert per_missing_element(A) == 1


def test_c_2():
    A = [2, 3, 4, 5]
    assert per_missing_element(A) == 1
