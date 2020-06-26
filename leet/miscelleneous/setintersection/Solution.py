#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sun 17:00:00 Sep 15 2019
@author : manoj

This module contains the different solutions for Inner Median for the given
two lists by following the below steps.
a) Step-1: Gets the "set-intersection" for the given two lists. The concept of
Set intersection can be found here.
    (https://en.wikipedia.org/wiki/Intersection_(set_theory)

b) Step-2: Inner median of the intersection set.
"""

import logging
logger = logging.getLogger('SetIntersectionLogger')
logger.setLevel(logging.INFO)


class InnerMedian:
    """
    Set Intersection for the given two lists
            Cases to Handle:
        1) Duplicates
        2) Unsorted
        3) Empty elements
        4) Negative Integers
    """
    def __init__(self):
        logger.info(f"Initializing InnerMedian Class: \n")

    @staticmethod
    def get_median_of_an_array(intersection):
        """

        Returns:

        """
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

    def get_inner_median_using_smaller_list(self, x, y):
        """



        Time Complexity: O(2k+klog(k)) - Sum of complexities of if-else
                         block and for loop. The other operations are O(1).
        Space Complexity : O(k)
        Args:
            list1:
            list2:

        Returns:

        """
        n = len(x)
        m = len(y)
        # if-else block: say k = min(n,m) , then complexity is O(k)
        # O(n) will be used to convert list to set
        if n <= m:
            smaller_list, larger_list = set(x), y
        else:
            smaller_list, larger_list = set(y), x
        # for loop: say k = min(n,m) then complexity is O(k + klog(k))
        intersection = sorted([val for val in smaller_list if val in \
                                                             larger_list])
        inner_median = self.get_median_of_an_array(intersection)
        return inner_median


    def get_inner_median_using_built_in_intersection(self, x, y):
        """
        Ref: https://docs.python.org/2/library/sets.html#set-objects
        Time Complexity: O(m*n)
        Returns:

        """
        #intersection = list(set(self.x) & set(self.y))
        intersection = sorted(list(set(x).intersection(y)))
        inner_median = self.get_median_of_an_array(intersection)
        return inner_median

    def get_inner_median_using_selection_algorithm(self, x, y):
        """
        To achieve the time complexity in O(n) and space complexity in O(1) for
        sorted.
        Idea1:To use the concept of MedianOfMedians and Selection Algorithm

        Ref1: https://en.wikipedia.org/wiki/Selection_algorithm
        Ref2: https://en.wikipedia.org/wiki/Median_of_medians#Algorithm

        Idea2: While forming the intersection, we have to find the median at
        the same time similar to problem 'median of two sorted arrays'. The
        trick here is to handle unsorted character of the arrays.
        Returns:
            median

        """
        # to be implemented.
        pass

    def get_inner_median_using_dynamic_programmin(self):
        """
        Similar to Longest Common Subsequence problem using DP.
        But, it ends up in O(mn) time complexity
        """
        pass
