"""Test BinaryGap"""


from lib.binary_gap import binary_gaps, convert_to_bin_number, remove_ending_zeros_f


def test_one():
    result = binary_gaps(1)
    assert result == 0


def test_two():
    result = binary_gaps(8)
    assert result == 0


def test_two_2():
    result = binary_gaps(9)
    assert result == 2


def test_t():
    result = binary_gaps(32)
    assert result == 0


def test_three():
    result = binary_gaps(20)
    assert result == 1

def test_four():
    result = binary_gaps(529)
    assert result == 4


def test_five():
    result = binary_gaps(561892)
    assert result == 3

def test_six():
    result = binary_gaps(1376796946)
    assert result == 5


def test_remove_zero():
    result = remove_ending_zeros_f("1000")
    assert result == "1"


def test_remove_zero_two():
    result = remove_ending_zeros_f("10100")
    assert result == "101"


def test_remove_zero_three():
    result = remove_ending_zeros_f('10001001001011100100')
    assert result == "100010010010111001"


def test_convert_to_bin_one():
    result = convert_to_bin_number(2)
    assert result == '10'


def test_convert_to_bin_two():
    result = convert_to_bin_number(5)
    assert result == '101'


def test_convert_to_bin_eight():
    result = convert_to_bin_number(8)
    assert result == '1000'


def test_convert_to_bin_three():
    result = convert_to_bin_number(128)
    assert result == '10000000'


def test_convert_to_bin_four():
    result = convert_to_bin_number(561892)
    assert result == '10001001001011100100'
