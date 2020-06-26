class Solution:
    """
    1. Iterate [start_org, end_org] from the interval list and check it against newInterval
    [start_new, end_new].
    if end_org < newInterval[0],
        append in [start_org, end_org] and continue to check the next.
    elif newInterval[1] < start_org,
        append in newInterval and then [start_org, end_org]
    else merge interval by appending
        in [min(start_new, start_org), max(end_org, end_new)].
    If the newInterval is merged or appended, check the last interval in
    result list against the remaining intervals.
Use a variable to mark if the newInterval is appened or merged.
If newInterval is not merged about iterating the entire input intervals, append it to the last of intervals
Time: O(n)
Space: O(1)
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]

        res = []
        inserted = False
        for start_org, end_org in intervals:
            if not inserted:
                if end_org < newInterval[0]:
                    res.append([start_org, end_org])
                elif newInterval[1] < start_org:
                    res.append(newInterval)
                    res.append([start_org, end_org])
                    inserted = True
                else:  # Merge
                    res.append([min(start_org, newInterval[0]), max(end_org, newInterval[1])])
                    inserted = True
            else:
                if res[-1][1] < start_org:
                    res.append([start_org, end_org])
                else:  # Merge
                    res[-1][1] = max(res[-1][1], end_org)
        if not inserted:
            res.append(newInterval)
        return res