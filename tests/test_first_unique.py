"""Test First Unique module"""


from lib.first_unique import first_unique


def test_example_one():
    a = [4, 10, 5, 4, 2, 10]
    expected_result = 5
    result = first_unique(a)
    assert result == expected_result


def test_example_two():
    a = [1, 1, 2, 2]
    expected_result = -1
    result = first_unique(a)
    assert result == expected_result


def test_example_three():
    a = [1,4,3,3,1,2]
    expected_result = 4
    result = first_unique(a)
    assert result == expected_result


