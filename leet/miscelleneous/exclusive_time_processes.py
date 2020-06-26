"""
Given a list of processes that can run in parallel. Each process is
represented by a triplet [id, startTime, endTime].

A process's exclusive time is the time spent to execute this process.
Note that this does not include the time while multiple processes run
simultaneously. Return the exclusive time of each process in the form [id, duration].
"""


def exclusive_time_process(processes_list):
    output = []
    for i, current_process in enumerate(processes_list):
        current_idx, current_start, current_end = current_process
        for j, other_process in enumerate(processes_list):
            other_idx, other_start, other_end = other_process
            if other_start >= current_end or other_end <= current_start :
                # skip other process - thid does not overlap with current
                continue
            else:
                # there is an overlap with other process
                # cut down the interval
                if other_start < current_start and other_end > current_end:
                    # no time for exclusiveness
                    output.append([current_idx, 0])
                    break
                elif other_start < current_start and other_end < current_end:
                    current_start = other_end
                elif other_start > current_end and other_end > current_end:
                    current_end = other_end
                elif other_start > current_start and other_end < current_end:
                    # block out the sub-interval
                    pass

        else:
            continue
        break # only executed if inner loop executes break

def pairs(input):
    input = list(input)
    result = []
    for i in range(0,len(input)):
        for j in input[i+1:]:
            if (input[i] & j) == 0:
                result.append([input[i], j])
    return result


input = {1, 2, 6, 9, 3}
print(pairs(input))

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            seen = []
            for i in range(len(s)):
                if t[i] not in seen:
                    seen.append(t[i])
                    s = s.replace(s[i], t[i])
            if s == t:
                return True
        return False

obj = Solution()
print(obj.isIsomorphic("ab", "aa"))