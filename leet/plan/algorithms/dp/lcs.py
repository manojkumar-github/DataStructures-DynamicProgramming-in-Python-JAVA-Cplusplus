#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only


"""
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""


def get_sub_seq(seq1, seq2):
    sub_seq = ""
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                sub_seq += seq1[i]
    return sub_seq

def lcs(seq1, seq2):
    """

    Args:
        seq1:
        seq2:

    Returns:

    """
    table = [[None] * (len(seq1) + 1)] * (len(seq2) + 1)
    print(table)
    for i in range(len(seq1) + 1):
        for j in range(len(seq2) + 2):

            if i == 0 or j == 0:
                table[i][j] = 0
            elif seq1[i-1] == seq2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[len(seq1)-1][len(seq2)-2]


def lcs_ref(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]
    print(L)
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

print(lcs("ABCDGH","AEDFHR"))
#print(lcs_ref("ABCDGH","AEDFHR"))
#print(lcs("AGGTAB", "GXTXAYB"))

