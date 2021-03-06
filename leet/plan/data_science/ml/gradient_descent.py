#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only


"""
Ref: https://ml-cheatsheet.readthedocs.io/en/latest/gradient_descent.html

Gradient descent is an optimization algorithm used to minimize some
function by iteratively moving in the direction of steepest descent as
defined by the negative of the gradient. In machine learning, we use
gradient descent to update the parameters of our model. Parameters refer
 to coefficients in Linear Regression and weights in neural networks.


https://github.com/bfortuner/ml-glossary/tree/master/code

Learning rate
The size of these steps is called the learning rate.
With a high learning rate we can cover more ground each step,
but we risk overshooting the lowest point since the slope of the
hill is constantly changing. With a very low learning rate, we can
confidently move in the direction of the negative gradient since we are
recalculating it so frequently. A low learning rate is more precise,
but calculating the gradient is time-consuming, so it will take us a
very long time to get to the bottom.


A Loss Functions tells us how good our model is at making predictions
for a given set of parameters. The cost function has its own curve and
its own gradients. The slope of this curve tells us how to update our parameters to make the model more accurate.
"""