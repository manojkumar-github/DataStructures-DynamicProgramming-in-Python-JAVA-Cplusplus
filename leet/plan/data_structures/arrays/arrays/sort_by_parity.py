"""
Input: [3,1,2,4]
Output: [2,4,3,1]
"""

def sort_by_parity(alist):
    op_list = []
    for elem in alist:
        if elem % 2 == 0:
            # even - list.insert(index, object)
            op_list.insert(0, elem)
        else:
            # append at last
            op_list.append(elem)
    return op_list

alist = [3,1,2,4]
print(sort_by_parity(alist))