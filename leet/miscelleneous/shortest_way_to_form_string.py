"""
We are given two different String str1 and String str2:
str1: 'apple'
str2: 'alphabet'
Are we able to form str1 by str2,
through repeating str2 and selecting subarray multiple times?
In this case, Yes.

By repeating three times and select subarray as:
a-p-----, --p-----, -l----e-

Determine whether its applicable to form str1 by str2
If so, how many repeat times is enough
"""

def reform(str1, str2):

    reform = ""
    n_repetitions = 0
    curr_pos = 0
    N = len(str1)
    while curr_pos < N: # curr_pos = 2, N = 5
        k = 0
        is_valid_repetetion = False
        for i in range(curr_pos, len(str1)): # 2,5
            is_found = False
            for j in range(k,len(str2)): # (0,8)
                if str1[i] == str2[j]:
                    reform += str1[i]   # reform = "ap"
                    k = j + 1 # k = 3
                    is_found = True
                    is_valid_repetetion = True
                    break
            if not is_found:
                break
        if is_valid_repetetion:
            n_repetitions += 1
            curr_pos = len(reform)
        else:
            return None
    return n_repetitions


print(reform("apple", ""))



