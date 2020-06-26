#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only



def lis(array):

    N = len(array)

    table = [1] * N

    lis = 0
    for i in range(1, N):
        for j in range(i):
            if array[j] < array[i]:
                table[i] = max(table[j] + 1, table[i])
                if table[i] > lis:
                    lis = table[i]
    return lis

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(lis(arr))

