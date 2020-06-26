def lcs_dp(astring1, astring2):
    m = len(astring1)
    n = len(astring2)
    dp_matrix = [[None]*(n+1) for i in range(m+1)]
    for i in range (m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp_matrix[i][j] = 0
            elif astring1[i-1] == astring2[j-1]:
                dp_matrix[i][j] = dp_matrix[i-1][j-1] + 1
            else:
                dp_matrix[i][j] = max(dp_matrix[i-1][j], dp_matrix[i][j-1])
    return dp_matrix[m][n]

print(lcs_dp("AGGTAB", "GXTXAYB"))
