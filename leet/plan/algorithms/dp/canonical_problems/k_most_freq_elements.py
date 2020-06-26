"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from collections import Counter
import heapq



def k_most_freq(arr, k=2):
    counter = Counter(arr)
    return heapq.nlargest(k, counter.keys(), key=counter.get)


print(k_most_freq([1,1,1,2,2,3]))

