def quick_sort(A, start=None, end=None):
    if start is None:
        start = 0

    if end is None:
        end = len(A)

    if end - start <= 1:
        return

    d = partition(A, start, end)
    print A
    quick_sort(A, start, d)
    quick_sort(A, d + 1, end)

    return A


def partition(A, start, end):
    # TODO: move random element to the end
    x = A[end - 1]
    d = start

    for i in range(start, end - 1):
        if(A[i] < x):
            swap(A, i, d)
            d += 1

    swap(A, d, end - 1)
    return d


def swap(A, a, b):
    c = A[a]
    A[a] = A[b]
    A[b] = c


problem = [1, 12, 0, -4, 10, 15, 22, 2, 1, 3, 4, 2, 3, 3, 10, 15, 6, 7, 8, 9]
print quick_sort(problem)
