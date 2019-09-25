def merge_sort(problem):
    length = len(problem)
    # if the list is empty, no answer
    if length <= 0:
        return []
    # if we are down to the last element return it
    if length == 1:
        return problem

    # get the middle of th array
    mid = length // 2

    listA = problem[0:mid]
    listB = problem[mid:length]

    # print length, mid, listA, listB

    mergedA = merge_sort(listA)
    mergedB = merge_sort(listB)

    return merge(mergedA, mergedB)


def merge(listA, listB):
    sorted = []
    pointerA = 0
    pointerB = 0

    while 1 == 1:
        if pointerA < len(listA):
            valueA = listA[pointerA]
        else:
            valueA = None

        if pointerB < len(listB):
            valueB = listB[pointerB]
        else:
            valueB = None

        if valueA is None and valueB is None:
            break

        if valueA is None:
            sorted.append(valueB)
            pointerB += 1
            continue

        if valueB is None:
            sorted.append(valueA)
            pointerA += 1
            continue

        if valueA < valueB:
            sorted.append(valueA)
            pointerA += 1
        else:
            sorted.append(valueB)
            pointerB += 1
    return sorted


problem = [1, 12, 3, 10, 15, 6, 7, 8, 9]
print merge_sort(problem)
