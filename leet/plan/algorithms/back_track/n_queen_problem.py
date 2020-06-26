#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only


"""
1. N*N chessboard, N queen to be placed so that no two queens attack each other
2. To output a binary matrix where 1s are queens and 0s are empty squares
"""

"""
notes: backtrack vs greedy difference vs brute force?
"""

"""
1.
2. there could be different possible configurations? Print one among.
3. Constraints = N>3
4. Back tracking algorithm: 
     1) By following the rules, we try to place each queen one after 
     the other.
     2) a) Start placing the first queen at the first row in first column.
        b) try placing the other queens one after the other in each column 
        such that it does not clash with previous queens. (because this is a 
        N*N
        chessboard and N queens, we have atleast place one queen in one 
        different column)
        c) 
        place_queen(current_queen, previous_queens):

            while placing each queen, 
            if the 
            logic do not find a 
            square to 
            place in its column, come back to previous queen and change its 
            position.
            if the previous queen position cant be changed, do the above 
            step to previous-previous queen
        d) If we visit all rows in the first column with first queen and we 
        are not able to place N queens on the board successfully. Return 
        No solution.
5. n*n matrix initiated with all 0s. Here 0 means empty. n-d list
6. Complexity T(n) = n*T(n-1) + N*n  = O(N!), Space = O(n*n)
"""

"""
Points missed:
1) Is_Safe_function():
        Just looking at previous rows diagnoally and at current row
2) Did not strike how to navigate diagnolly
3) Unable to implement back-tracking using recursion
"""


def is_safe(board, row_ix, col_ix, n):

    # 1. check upper left diagnol
    for i, j in zip(range(row_ix, -1, -1), range(col_ix, -1 -1)):
        # checks from current box
        if board[i][j] == 1:
            return False

    # 2. check lower left diagnol
    for i, j in zip(range(row_ix, n, 1), range(col_ix, -1, -1)):
        # checks from current box as well
        if board[i][j] == 1:
            return False

    # 3. iterate all columns in this row
    for j in range(col_ix):
        if board[row_ix][j] == 1:
            return False
    return True



def is_configuration_exist(board, col_ix, N):

    if col_ix >= N:
        # we have filled all columns
        return True

    for row_ix in range(N):
        if is_safe(board, row_ix, col_ix, N):

            board[row_ix][col_ix] = 1
            # perform recursion to fill the next queen
            if is_configuration_exist(board, col_ix + 1, N) == True:
                return True
            # back-tracking step
            board[row_ix][col_ix] = 0
    return False

def printSolution(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print()

def n_queen_placer():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if is_configuration_exist(board, 0, 4) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

n_queen_placer()