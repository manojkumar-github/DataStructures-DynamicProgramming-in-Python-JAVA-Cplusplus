#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only


from collections import deque

def get_value(item_tuple):
    return item_tuple[1]

class Node:
    def __init__(self, level=None, profit=None, bound=None, weight=None):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight


def knapsack(thres_weight, item_tuple, n):
    """

    Args:
        thres_weight:
        item_tuple: (weight, value)
        n:

    Returns:

    """
    # sort item by value
    sorted_items = sorted(item_tuple, key=get_value)
    # start a queue
    node_queue = deque()
    # add a dummy node
    u = Node(level=-1, profit=0, bound=None, weight=0)
    v = Node()
    node_queue.append(u)

    # one by one extract an item from decision tree and compute profit
    # of all children of extracted item and keep saving maximum profit
    max_profit = 0
    while len(node_queue) > 0:
        u = node_queue.popleft()
        if u.level == -1:
            v.level = 0
        if u.level == n-1:
            continue
        # if the not the node from edges, then increment its level
        v.level = u.level + 1

        v.weight = u.weight  + item_tuple[v.level].weight
        v.profit = u.profit + item_tuple[v.level].value








