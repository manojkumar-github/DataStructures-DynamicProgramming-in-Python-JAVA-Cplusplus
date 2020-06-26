"""
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""

def get_sorted_array_squares(alist):
    """

    :param alist:
    :return:
    """
    return sorted(list(map(lambda x: x*x, alist)))

alist = [-4,-1,0,3,10]


print(get_sorted_array_squares(alist))