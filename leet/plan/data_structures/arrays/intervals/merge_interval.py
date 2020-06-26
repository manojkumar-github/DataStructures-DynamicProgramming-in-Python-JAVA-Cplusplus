"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def merge_intervals(intervals):
    intervals.sort(key=lambda interval:interval[0])
    N = len(intervals)
    index = 0
    while index < N - 1:
        if intervals[index][1] >= intervals[index + 1][1]:
            # this interval foot print is larger than the next one
            intervals.pop(index + 1)
            N -= 1
        elif intervals[index][1] >= intervals[index+1][0]:
            # merge second interval to first
            intervals[index][1] = intervals[index + 1][1]
            intervals.pop(index + 1)
            N -=1
        else:
            index += 1
    return intervals

print(merge_intervals([[1,4],[0,4]]))