"""
Input: [1,1,4,2,1,3]
Output: 3
"""

def height_checker(alist):
    this_max = max(alist)
    back_pos = 0
    for i in range(len(alist)-1):
        if alist[i] == this_max:
            alist[i],alist[back_pos-1] = alist[back_pos-1], alist[i]
            back_pos += 1
            this_max = alist[:len(alist) - back_pos]
    return alist

A = [1,1,4,2,1,3]

print(height_checker(A))
