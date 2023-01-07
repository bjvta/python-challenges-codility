"""Test Pairing"""


from lib.pairing_m import find_unpair, find_unpair_v2


def test_1():
    A = [9, 3, 9, 3, 9, 7, 9]
    expected = 7
    assert find_unpair_v2(A) == expected


def test_2():
    A = [1]
    expected = 1
    assert find_unpair_v2(A) == expected

def test_3():
    A = [9, 3, 9, 3, 9, 7, 9, 9, 3, 9, 3, 9, 7, 9, 7]
    expected = 7
    assert find_unpair_v2(A) == expected

