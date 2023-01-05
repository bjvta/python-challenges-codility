"""First Unique module"""

import array as arr


def first_unique(lst):
    counts = {}

    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for item in lst:
        if counts[item] == 1:
            return item

    return -1
