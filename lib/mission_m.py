"""Mission dev"""


def sum_mul_4(A):
    a = []
    for ele in A:
        if ele % 4 == 0:
            a.append(ele)
    return sum(a)


def min_changes(A):
    if len(A) > 0:
        count1 = 0
        count2 = 0
        for i in range(len(A)):
            if i % 2 == 0:
                if A[i] == 1:
                    count1 += 1
                if A[i] == 0:
                    count2 += 1
            else:
                if A[i] == 0:
                    count1 += 1
                if A[i] == 1:
                    count2 += 1
        return min(count1, count2)
    return 0
