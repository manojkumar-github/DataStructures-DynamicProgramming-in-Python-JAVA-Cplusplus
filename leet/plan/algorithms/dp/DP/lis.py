#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only


seq = [3, 10, 2, 1, 20]


"""
3 -
  1) 3, 10
  2) 3, 20
  

10
 - 10, 20
 
2 - 
   2, 20
   
1 -
  1, 20


"""


def LIS(seq):
    max_seq = 0
    for each_num in seq:
        sub_seq = "give me all increasing subsequences"
        this_sub_seq_len = len(sub_seq)
        if this_sub_seq_len > max_seq:
            max_seq = this_sub_seq_len



    return max_seq