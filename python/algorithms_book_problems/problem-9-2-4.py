# RANDOMIZED-SELECT(A, start, end, search)
#   if start == end
#       return A[start]
#   pivot = RANDOMIZED-PARTITION(A, start, end)
#   current = pivot - start + 1 # + 1 because of zero array
#   if search == current // the pivot value is the answer
#       return A[pivot]
#   elseif search < current
#       return RANDOMIZED-SELECT(A, start, pivot - 1, search)
#   else
#       return RANDOMIZED-SELECT(A, pivot + 1, end, search - current)

# RANDOMIZED-PARTITION(A, start, end)
#   current = RANDOM(start, end)
#   swap(A, current, end)
#   return PARTITION(A, start, end)

# PARTION(A, start, end)
#   mid = A[end]
#   current = start - 1
#   for i from start to end - 1
#       if i <= mid
#           current += 1
#           swap(A, current, i)
#   current += 1
#   swap(A, current, end)
#   return current

import random


def findSelectedMin(A, search, start=None, end=None):
    length = len(A)
    if length == 0 or start >= length:
        return None

    if start is None:
        start = 0
    if end is None:
        end = len(A)

    print A, start, end

    if start == end:
        return A[start]

    mid = randomPartition(A, start, end)
    current = mid + 1
    if current == search:
        return A[mid]

    if current > search:
        return findSelectedMin(A, search, start, mid)
    else:
        return findSelectedMin(A, search, mid + 1, end)


def findNthMin(A, search):
    if len(A) == 0 or search >= len(A):
        return None

    start = 0
    end = len(A)
    value = None
    while start < end:
        mid = randomPartition(A, start, end)
        current = mid + 1
        if current == search:
            value = A[mid]
            break
        elif current > search:
            end = mid
        else:
            start = mid + 1

    return value


def randomPartition(A, start, end):
    r = random.randint(start, end - 1)
    # print 'random:', r
    swap(A, r, end - 1)

    mid = A[end - 1]
    current = start - 1

    for i in range(start, end - 1):
        if A[i] <= mid:
            current += 1
            swap(A, current, i)

    current += 1
    # print 'current:', current, A
    swap(A, current, end - 1)
    # print 'mid:', current, A

    return current


def swap(A, d, b):
    c = A[d]
    A[d] = A[b]
    A[b] = c


problem = [1, 2, 34, 5, 10, 6, 7, 8, 9, 4]
search = 23
print problem, 'find:', search

print findNthMin(problem, search)
