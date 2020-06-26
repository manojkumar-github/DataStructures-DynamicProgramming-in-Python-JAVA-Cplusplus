#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
- N activites with start and finish times
- Max num of activities that can be performed by a single person
- A person can work one activity at a time

Ex 1:
start = [10, 12, 20]
finish = [20, 25, 30]

Solution: Atmost 2 activites can be performed [(10,20), (20,30)]

Algorithm: (Greedy Algorithm)
    1) Sort by finish time
    2) Pick those activites where start time of current activity is greater
    than previous activities'  finish time
"""

"""
1. We have sorted finish times
"""

def activity_selection_finish_time_sorted(start_times, finish_times_sorted):
    """
    Algorithm Paradigmn: Greedy
    Complexity:
        a) Time : O(n)
    Args:
        start_times(list):
        finish_times_sorted(list):

    Returns:
        int: N of activities
    """
    previous_finish_time = 0
    n = 0
    for (start_time, finish_time) in zip(start_times, finish_times_sorted):
        if start_time > previous_finish_time:
            n += 1
            previous_finish_time = finish_time
    return n

# Test case for above function

s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]

assert 4 == activity_selection_finish_time_sorted(s, f)

"""
2. We do not have sorted finish times
"""




# test case for the above function

def get_finish_time(a_tuple):
    return a_tuple[1]

def activity_selection_finish_time_not_sorted(activity_arr):
    """
    Greedy Solution
    Complexity:
        a) Time: O(nlogn), extra log(n) came for sorting the function
        b) Space: O(n), atmost we will end up selecting all the activities.
    1. Sort the activity array on finish times
    2. And repeat the above function
    Args:
        activity_arr(list):

    Returns:
        list: activities selected

    """
    # Sort a list of tuples based on second index
    activity_arr.sort(key=get_finish_time)
    previous_finish_time = 0
    selected_activites = []
    for (start_time, finish_time) in activity_arr:
        if start_time > previous_finish_time:
            selected_activites.append((start_time, finish_time))
            previous_finish_time = finish_time
    return selected_activites


activity_arr = [(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]
print(activity_selection_finish_time_not_sorted(activity_arr))













