"""Test Cycling module"""


from lib.cycling_m import cycling_f


def test_one():
    A = [3, 8, 9, 7, 6]
    K = 3
    expected = [9, 7, 6, 3, 8]
    assert cycling_f(A, K) == expected


def test_two():
    A = [0,0,0]
    K = 1
    expected = [0,0,0]
    assert cycling_f(A, K) == expected


def test_three():
    A = [1,2,3,4]
    K = 4
    expected = [1,2,3,4]
    assert cycling_f(A, K) == expected


def test_4():
    A = []
    K = 4
    expected = []
    assert cycling_f(A, K) == expected


def test_5():
    A = [-4,-4,-3,-2,-2,-1,0,2,3,4,5,6,6]
    K = 26
    expected = [-4,-4,-3,-2,-2,-1,0,2,3,4,5,6,6]
    assert cycling_f(A, K) == expected

