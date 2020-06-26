#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only
"""
Given a gold mine of n*m dimensions. Each field in this mine contains a
positive integer which is the amount of gold in tons. Initially the miner
is at first column but can be at any row.

He can move only (right->,right
up /,right down\) that is from a given cell, the miner can move to the cell
 diagonally up towards the right or right or diagonally down towards the
 right. Find out maximum amount of gold he can collect.

Examples:

Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12
{(1,0)->(2,1)->(2,2)}



"""

"""
(0,0)       -> (0,1)    -> (0,2) = 7
                        -> (1,2) = 8
            -> (1,1)    -> (0,2) = 5
                        -> (1,2) = 7
                        -> (2,2) = 6
(1,0)       -> (0,1)    -> (0,2) = 8
                        -> (1,2) = 9
            -> (1,1)    -> (0,2) = 6
                        -> (1,2) = 7
                        -> (2,2) = 7
            -> (2,1)    -> (1,2) = 12
                        -> (2,2) = 12
(2,0)       -> (1,1)    -> (0,2) = 4
                        -> (1,2) = 5
                        -> (2,2) = 5
            -> (2,1)    -> (1,2) = 10
                        -> (2,2) = 10

Top Down Approach
"""


def get_max_sum(store, mat, i, j):
    if i == 0:
        max_prev_field = max(store[(i, j-1)] ,
                             store[(i+1, j-1)])
    elif i == len(mat) - 1:
        max_prev_field = max(store[(i-1, j-1)] ,
                             store[(i, j-1)])
    else:
        max_prev_field = max(store[(i-1, j-1)] ,
                             store[(i, j-1)], store[(i+1, j-1)])
    return max_prev_field + mat[i][j]

def get_max_gold(mat, m, n):
    store = {(i, j): mat[i][j] for i in range(len(mat)) for j in range(len(mat[
                                                         0]))}
    print(store)
    max_val = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j == 0:
                store[(i,j)] = mat[i][j]
            else:
                store[(i, j)] = get_max_sum(store, mat, i, j)
            if store[(i,j)] > max_val:
                max_val = store[(i,j)]
    return max_val

matrix = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]

print(get_max_gold(matrix, 3, 3))


