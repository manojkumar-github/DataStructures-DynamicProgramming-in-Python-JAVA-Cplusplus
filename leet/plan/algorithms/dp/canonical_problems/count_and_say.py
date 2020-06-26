#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
count-and-say sequence. You can do so recursively, in other words
from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups
"2" and "1", "2" can be read as "12" which means frequency = 1 and
value = 2, the same way "1" is read as "11", so the answer is the
concatenation of "12" and "11" which is "1211".
"""


def build_current_num(prev_num_string):
    """
    "12 1 1"
    Args:
        prev_num(string):

    Returns:

    """
    count = 1
    new_num_str = "" # 1112
    for index, curr_digit in enumerate(prev_num_string): # curr = "1", index=3
        if index == 0:
            prev_digit = None # first digit case
        else:
            prev_digit = prev_num_string[index-1] # prev = 1
        if prev_digit == None:
            continue
        elif prev_digit == curr_digit: # 1 == 1
            count += 1
        else:
            new_num_str += str(count) # 1
            new_num_str += prev_digit

    new_num_str += str(count)
    new_num_str  += prev_num_string[-1]

    return new_num_str


def nth_term_count_and_say(n):
    """

    Args:
        n(int):

    Returns:

    Algorithm:
    1) Look at previous num and
    2) build the current number


    """
    if  n < 1 or n > 30:
        # constraints
        raise Exception("Not supported:")

    if n == 1:
        return "1"

    prev_num = "1"
    curr_num_str = ""
    # iterative approach
    for num in range(2, n+1):
        # build the current number
        curr_num_str = build_current_num(prev_num)
        prev_num  = curr_num_str
    return curr_num_str

print(nth_term_count_and_say(5))

