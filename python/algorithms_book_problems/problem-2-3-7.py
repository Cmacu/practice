# 2.3-7
# Describe a (n lg n) time algorithm that, given a set S of n integers and another integer x, determines whether or not there exist two elements in S whose sum is exactly x.

from collections import Counter
list = [1, -19, 30, 6, 5, 1, 7, 8]
sum = 11
print list

# BRUTE FORSE n^2
# found = False
# for i in range(len(list)):
#     for j in range(i+1, len(list)):
#         if list[i] + list[j] == sum:
#             found = True
#             break
#     if found:
#         break

# print i, j
# print list[i], list[j],

# SORT AND SEARCH 2n lg n
# list.sort()
# print list
# left = 0
# right = len(list) - 1

# while left < right:
#     if list[left] + list[right] > sum:
#         right -= 1
#     elif list[left] + list[right] < sum:
#         left += 1
#     else:
#         break

# HASH TABLE
dict = {}

left = right = 0
for i in range(len(list)):
    rightValue = list[i]
    leftValue = sum - rightValue
    print rightValue, leftValue
    if dict.get(leftValue) is not None:
        right = i
        left = dict[leftValue]
        break
    else:
        dict[rightValue] = i

print dict

print left, right
if left < right:
    print 'Elements found (' + str(left) + ',' + str(right) + '): ' + \
        str(list[left]) + ' + ' + str(list[right]) + ' = ' + str(sum)
else:
    print 'Sum of ' + str(sum) + ' not found'
