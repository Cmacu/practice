problem = [1, 12, 0, 10, 15, 22, 2, 1, 3, 4, 2, 3, 3, 10, 15, 6, 7, 8, 9]
print problem


def count_sort(A, k):
    length = len(A)
    C = [0] * k

    for i in A:
        C[i] += 1

    for j in range(1, k):
        C[j] = C[j-1] + C[j]

    B = [None] * length

    # print C

    for d in range(length-1, -1, -1):
        value = A[d]
        posInC = value
        posInB = C[posInC] - 1
        B[posInB] = value
        # decrease count
        C[posInC] -= 1

    return B


print count_sort(problem, 30)
