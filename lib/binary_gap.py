"""BinarGap"""

def binary_gaps(number):
    binary_number = convert_to_bin_number(number)
    binary_number = remove_ending_zeros_f(binary_number)
    zeros = binary_number.split('1')
    zeros = list(filter(None, zeros))
    if len(zeros) < 1:
        return 0
    zeros = sorted(zeros)
    return len(zeros[-1])


def remove_ending_zeros_f(num):
    last_char = num[-1]
    while last_char == '0':
        num = num[:-1]
        last_char = num[-1]

    return num


def convert_to_bin_number(n):
    bin_number = ""
    digit = 2
    while n >= digit:
        res = n % digit
        n = n / digit
        bin_number = f"{int(res)}{bin_number}"

    res = n % digit
    bin_number = f"{int(res)}{bin_number}"
    return bin_number
