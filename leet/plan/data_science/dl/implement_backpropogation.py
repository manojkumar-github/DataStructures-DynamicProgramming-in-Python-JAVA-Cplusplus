#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
In deep learning, backpropagation computes the gradient of the loss
function with respect to the weights of the network for a single input–output
example, and does so efficiently, unlike a naive direct computation of the
 gradient with respect to each weight individually. This efficiency makes
  it feasible to use gradient methods for training multilayer networks,
  updating weights to minimize loss; gradient descent, or variants such as
   stochastic gradient descent, are commonly used. The backpropagation
   algorithm works by computing the gradient of the loss function with
   respect to each weight by the chain rule, computing the gradient one
   layer at a time, iterating backward from the last layer to avoid redundant
   calculations of intermediate terms in the chain rule; this is an example
   of dynamic programming
"""

"""
1. Transfer derivative
2. Error Backpropogation
"""