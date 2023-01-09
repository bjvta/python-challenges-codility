"""Test Mission module"""


from lib.mission_m import min_changes, sum_mul_4


def test_one_1():
    A = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]
    assert sum_mul_4(A) == -16


def test_one_2():
    A = [-6, -91, 1011, -100, 84, -22, 0, 1, 473, -6, -91, 1011, -100, 84, -22, 0, 1, 473]
    assert sum_mul_4(A) == -32



def test_two_1():
    A = [1, 0, 1, 0, 1, 1]
    assert min_changes(A) ==  1


def test_two_2():
    A = [1, 1, 0, 1, 1]
    assert min_changes(A) ==  2


def test_two_3():
    A = [0, 1, 0]
    assert min_changes(A) ==  0


def test_two_4():
    A = [0, 1, 1, 0]
    assert min_changes(A) ==  2


def test_two_5():
    A = [0]
    assert min_changes(A) ==  0

