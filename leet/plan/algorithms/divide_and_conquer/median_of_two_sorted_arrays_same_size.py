#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

arr1 = [1, 12,15, 26, 38]
arr2 = [2, 13, 17, 30 , 45]

def get_median_two_sorted_arrays_merge_sort(arr1, arr2):
    """
    Time complexity: O(m+n)
    Space complexity: O(n)
    Args:
        arr1:
        arr2:

    Returns:

    """

    new_arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        new_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        new_arr.append(arr2[j])
        j += 1

    N = len(new_arr)
    mid = len(new_arr)//2
    if N %2 == 0:
        return (new_arr[mid] + new_arr[mid-1])/2
    else:
        return new_arr[mid]

print(get_median_two_sorted_arrays_merge_sort(arr1, arr2))

def o_n_solution(arr1, arr2):
    """
    Time complexity: Half merge sort i.e half of O(2n) = O(n)
    Args:
        arr1:
        arr2:

    Returns:

    """
    new_arr = []
    i = 0
    j = 0
    n = len(arr1)
    while len(new_arr) < n + 1 and i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    return (new_arr[n-1] + new_arr[n]) /2

print(o_n_solution(arr1, arr2))


def getMedian(arr1, arr2, n):
    # there is no element in any array
    if n == 0:
        return -1

    # 1 element in each => median of
    # sorted arr made of two arrays will
    elif n == 1:
        # be sum of both elements by 2
        return (arr1[0] + arr2[1]) / 2

    # Eg. [1,4] , [6,10] => [1, 4, 6, 10]
    # median = (6+4)/2
    elif n == 2:
        # which implies median = (max(arr1[0],
        # arr2[0])+min(arr1[1],arr2[1]))/2
        return (max(arr1[0], arr2[0]) +
                min(arr1[1], arr2[1])) / 2

    else:
        # calculating medians
        m1 = median(arr1, n)
        m2 = median(arr2, n)

        # then the elements at median
        # position must be between the
        # greater median and the first
        # element of respective array and
        # between the other median and
        # the last element in its respective array.
        if m1 > m2:

            if n % 2 == 0:
                return getMedian(arr1[:int(n / 2) + 1],
                                 arr2[int(n / 2) - 1:], int(n / 2) + 1)
            else:
                return getMedian(arr1[:int(n / 2) + 1],
                                 arr2[int(n / 2):], int(n / 2) + 1)

        else:
            if n % 2 == 0:
                return getMedian(arr1[int(n / 2 - 1):],
                                 arr2[:int(n / 2 + 1)], int(n / 2) + 1)
            else:
                return getMedian(arr1[int(n / 2):],
                                 arr2[0:int(n / 2) + 1], int(n / 2) + 1)

                # function to find median of array


def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n / 2)] +
                arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n / 2)]

print(getMedian(arr1, arr2, len(arr1)))















