# Let A[1::n] be an array of n distinct numbers. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A
# Give an algorithm that determines the number of inversions in any permutation on n elements in (n lg n) worst-case time.
# (Hint: Modify merge sort.)

list = [10, 2, 3, 8, 6, 4, 1, 2, 3, 4, 5]  # 9+1+2+6+5 = 23
print list

# BRUTE FORCE
length = len(list)
count = 0
for i in range(length):
    for j in range(i+1, length):
        if list[i] > list[j]:
            count += 1

print 'Brute force: ', count


# MERGE COUNT
def inversionCount(start=0, end=len(list)):
    count = 0
    # print start, end
    length = end - start
    if length < 2:
        return count

    mid = start + length // 2
    count += inversionCount(start, mid)
    count += inversionCount(mid, end)

    for i in range(start, mid):
        for j in range(mid, end):
            if list[i] > list[j]:
                count += 1

    return count


print 'Merge count: ', inversionCount()


# MERGE SORT COUNT

def mergeCount(list):
    length = len(list, )
    if length <= 1:
        return list, 0

    mid = length // 2
    left, countLeft = mergeCount(list[0:mid])
    right, countRight = mergeCount(list[mid:length])
    count = countLeft + countRight

    sorted = []
    max = float('inf')
    l = r = 0
    while l < len(left) or r < len(right):
        leftValue = left[l] if l < len(left) else max
        rightValue = right[r] if r < len(right) else max
        if leftValue > rightValue:
            sorted.append(rightValue)
            count += len(left) - l
            r += 1
        else:
            sorted.append(leftValue)
            l += 1

    return sorted, count


sorted, count = mergeCount(list)
print 'Merge sort: ', count
