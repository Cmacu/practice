import math

problem = [0.78, 1, 0.17, 0.40, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print problem


def bucket_sort(A, buckets=10):
    B = [None] * (buckets + 1)
    for i in A:
        d = math.trunc(i / (1 / float(buckets)))
        B[d] = B[d]
        if B[d] is None:
            B[d] = []
        B[d].append(i)

    C = []
    for bucket in B:
        if bucket is None:
            continue
        length = len(bucket)
        for i in range(length):
            for j in range(i+1, length):
                if bucket[i] > bucket[j]:
                    swap(bucket, j, i)

        for i in bucket:
            C.append(i)

    return C


def swap(A, a, b):
    c = A[a]
    A[a] = A[b]
    A[b] = c


print bucket_sort(problem)
