#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
Weighted Job Scheduling:
Given N jobs:
    - Start time
    - Finish time
    - Profit associated(>=0)
Question: Find the maximum profit subsets that do not overlap

Algorithm 1: Recursive Solution
    1) Sort the jobs on finish time.
    2) Get the maximum-profit including current job
    3) Get the maximum-profit excluding current job
    4) Get the maximum of profits from step-2 and step-3

"""




def dp_solution(activities_arr):
    """
    ref: https://www.youtube.com/watch?v=cr6Ip0J9izc

    Solution:
        1) Have a table so size N_jobs
        2) For each job:
            - iterate from jobs to till this job and find those jobs which
            does not overlap with current job
            - if this job profit + previous non-overlapping max profit >
            profit till last job

    Returns:

    """
    profit_at_this_job_dp_table = [None] * len(activities_arr)

    profit_at_this_job_dp_table[0] = activities_arr[0][2]
    for i in range(1, len(activities_arr)):
        # initiate the profit of the current job to the table
        profit_at_this_job_dp_table[i] = max(activities_arr[i][2],
                                             profit_at_this_job_dp_table[i-1])
        for j in range(0, i):
            if activities_arr[j][1] <= activities_arr[i][0]:
                # maximum of current profit and (sum of current profit and
                # previous job non-overlapping profit)
                profit_at_this_job_dp_table[i] = max(profit_at_this_job_dp_table[i], activities_arr[i][2] +
                                                     profit_at_this_job_dp_table[j])

    print(profit_at_this_job_dp_table)

    return max(profit_at_this_job_dp_table)





print(dp_solution([(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]))
print(dp_solution([(3, 10, 20), (1, 2, 50), (6, 19, 100), (2, 100, 200)]))
print(dp_solution([(1, 3, 5), (2, 5, 6), (4, 6, 5), (6,7,4), (5,8,11), (7,9,
                                                                        2)]))