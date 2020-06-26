#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
Given an array of meeting time intervals consisting of start and end times
[[s1, e1]] find the minimum number of conference rooms required.

Example:
    Input : [[0,30], [5,10], [15,20]]
    Output: 2


    Input: [[7,10], [2,4], [3,15], [6,20]]


            = [[2,4], [3,15], [6,20], [7,10]
    Output: 3

"""

"""
1. Sort on start times (index1 of list)
2. rooms = 1  (latest end time) = 4 [6,20] 20
           1  (latest end time) = 15     15           = 15
            
        
"""

def first_elem(alist):
    return alist[0]







def get_first_elem(alist):
    return alist[0]

def min_meeting_rooms(intervals):
    """

    Args:
        intervals:

    Returns:

    """
    intervals.sort(key=get_first_elem) # O(nlogn)

    n_meeting_rooms = 1
    # fifo
    priority_queue = []

    for start, end in intervals:
        if priority_queue:
            latest_end_time = priority_queue.pop(0)
        else:
            latest_end_time = 0
        if start < latest_end_time:
            n_meeting_rooms += 1
            priority_queue.insert(0, min(latest_end_time, end))
        priority_queue.append(end)
    return n_meeting_rooms

#print(min_meeting_rooms([[7,10], [2,4], [3,15], [6,20]]))
#print(min_meeting_rooms( [[0,30], [5,10], [15,20]]))
#print(min_meeting_rooms([[7,10], [2,4]]))






