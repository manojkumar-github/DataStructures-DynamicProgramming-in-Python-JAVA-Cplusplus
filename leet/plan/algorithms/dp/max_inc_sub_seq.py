#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

import copy

def mis(array):

    N = len(array)

    table = copy.deepcopy(array)

    mis = 0
    for i in range(1, N):
        for j in range(i):
            if array[j] < array[i]:
                table[i] = max(table[j] + array[i], table[i])
                if table[i] > mis:
                    mis = table[i]
    return mis

arr = [1, 101, 2, 3, 100, 4, 5]
print(mis(arr))

