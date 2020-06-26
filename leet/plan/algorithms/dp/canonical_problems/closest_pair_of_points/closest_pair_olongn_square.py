#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
Closest Pair of points:
1. O(nlogn) using Divide and Conquer
2. Divide:
    Split the plane into two halfs and Recursively find the pair of points
    closest in each half
3. Merge
    d = min(d_left, d_right), d would be the answer but
4. Sy be the plane which is distance "d" on both sides
    - sort the points by decreasing y-coordinate
    
"""