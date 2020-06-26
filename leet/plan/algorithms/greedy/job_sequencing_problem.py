#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
jobs = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27],
        ['d', 1, 25], ['e', 3, 15]]
"""


def get_third_item(alist):
    return alist[2]

def job_scheduler(jobs, t):

    """
    1. Sort all jobs by deadline
    2. Pick jobs that match the criteria
    3. Time complexity: O(n^2)
    Args:
        jobs:

    Returns:

    """

    jobs.sort(key=get_third_item, reverse=True)
    selected = [jobs[0][0]]
    time_index = 2
    i = 1
    while time_index <= t and i < len(jobs):

        curr_job_deadline, curr_job_profit = jobs[i][1], jobs[i][2]
        if curr_job_deadline >= time_index:
            # include job
            selected.append(jobs[i][0])
            time_index += 1
        i +=1
    return selected

jobs = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27],
        ['d', 1, 25], ['e', 3, 15]]

print(job_scheduler(jobs, 3))









