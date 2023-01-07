"""Cycling module"""


def cycling_f(A, K):
    if len(A) == 0 or K == 0:
        return A
    i = 0
    while i < K:
        A = [A[-1]] + A[:-1]
        i += 1
    return A
