#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only
"""
: set[] = {3, 34, 4, 12, 5, 2}, sum = 9

[1,4,11,3,2,1]   sum = 4

1,1,2
4
3,1
"""

"""
1,4 1,11, 1,3 1,2 1,11
"""

def is_subsets_sum(alist, sum):

    for i in range(len(alist)):
        curr_sum = alist[i]
        subset = [alist[i]]
        for j in range(i+1, len(alist)):

            curr_sum += alist[j]
            if curr_sum  > sum:
                curr_sum -= alist[j]
            elif curr_sum < sum:
                subset.append(alist[j])
            else: # equals case
                subset.append(alist[j])
                print(subset)
                subset = [alist[i]]
                curr_sum -= alist[j]
    return False

#print(is_subsets_sum([3,34,4,12,5,2], 9))
print(is_subsets_sum([1,4,11,3,2,1], 4))














