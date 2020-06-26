# TODO: Test cases - edge cases, key functions
# TODO: Efficiencies in space and time O(n) and space


"""
Test cases:
1. Sorted vs Unsorted
2. Integers positive negative (no decimals)
"""
def inner_median(x, y):
    """
    Returns the median of the set intersection of two lists of integers. Ex:
    inner_median([1,2,3], [2,3,3]) would return 2.5 ([2,3] is the intersection
    of x, y and 2.5 is the median of [2,3]).
    x (list<int>): A list of integers.
    y (list<int>): A list of integers.
    """
    intersection = []
    # get intersection set
    for x_val in x:
        for y_val in y:
            if y_val == x_val:
                intersection.append(x_val)
    # no intersection
    if len(intersection) == 0:
        raise ValueError("There were no common elements in x, y")
    # odd: get mid-point
    elif len(intersection) % 2 != 0:
        return float(intersection[int(len(intersection) / 2)])
    # even: average mid-points
    else:
        mid_a = intersection[int(len(intersection) / 2) - 1]
        mid_b = intersection[round(len(intersection) / 2)]
        return float(mid_a + mid_b) / 2

print(inner_median([3,1,2], [1,2,3,4]))
print(inner_median([1,3,2,1,3], [1,2,3,4]))
print(inner_median([1,1,3,2,1,3], [1,2,3,4]))



