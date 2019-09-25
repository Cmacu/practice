import math

problem = [110, 1200, 1021, 102, 15, 2, 2000, 1111, 3321,
           422, 233, 321, 3332, 1032, 1532, 632, 754, 8644, 932]
print problem


def redix_sort(A):
    hasDigits = True
    digit = 0
    while hasDigits:
        digit += 1
        A, hasDigits = count_sort(A, 10, digit)

    return A


def count_sort(A, k, digit):
    length = len(A)
    C = [0] * k

    hasDigits = False
    for i in A:
        currentDigit = get_current_digit(i, digit)
        if currentDigit > 0:
            hasDigits = True
        C[currentDigit] += 1

    if hasDigits is False:
        return A, False

    for j in range(1, k):
        C[j] = C[j-1] + C[j]

    B = [None] * length

    # print C

    for d in range(length-1, -1, -1):
        value = get_current_digit(A[d], digit)
        posInC = value
        posInB = C[posInC] - 1
        B[posInB] = A[d]
        # decrease count
        C[posInC] -= 1

    return B, True


def get_current_digit(number, digit):
    reminder = math.fmod(number, math.pow(10, digit))
    current_digit = reminder / math.pow(10, digit - 1)
    return math.trunc(current_digit)


print redix_sort(problem)
