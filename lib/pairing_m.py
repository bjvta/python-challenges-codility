"""Pairing module"""


# This is a bad version of iterate a list
def find_unpair(A):
    i = 0
    while i < len(A):
        j = i+1
        while j < len(A):
            if A[i] == A[j]:
                del A[j]
                del A[i]
                i = 0
                j = i + 1
            else:
                j += 1
        i += 1
    return A[0]


def find_unpair_v2(A):
    s = set()
    for ele in A:
        s.add(ele) if ele not in s else s.remove(ele)
    return list(s)[0]
