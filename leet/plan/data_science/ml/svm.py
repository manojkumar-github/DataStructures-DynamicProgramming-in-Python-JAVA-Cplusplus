#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only


"""
Ref: https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/
Ref: https://scikit-learn.org/stable/modules/svm.html

Key points:
    - Supervised
    - Supports both classification and regression
    - Data is distributed in n-dimensional space (n-features)
    - Perform classification by finding the HYPER-PLANE that differentiates
    two classes well.
    - Support Vectors = co-ordinates of individual observation
    - Identifying right hyper plane
        - Pick the plane that is farthest from the nearest data-points(Margin)
    - Robust to outliers
    - KERNEL TRICK:
        - Converts non-seperable problem to seperable problem
        - Used for non-linear seperation problem
        - Does complex data-transformations for data seperation
        - Uses the function that transform low-dimensional space to higher
        dimensional spaces.

Advantages:
    - Effective in higher dimensional spaces
    - Effective in cases where dimensions are more than number of samples
    - Memory efficient: Uses a subset of training points
    - Versatile: Common kernals and customized kernals
    - Multi-Class classification: "one against one approach"
    - Unbalanced problems: tune class_weight parameter

Main Hyperparameters to tune:
    - C(default=1) : penality parameter. Should be reduced when there are many
                    noisy observations.

                    The C parameter tells the SVM optimization how much you
                    want to avoid misclassifying each training example.
                    For large values of C, the optimization will choose a
                    smaller-margin hyperplane if that hyperplane does a better
                    job of getting all the training points classified
                    correctly. Conversely, a very small value of C will cause
                    the optimizer to look for a larger-margin separating
                    hyperplane, even if that hyperplane misclassifies more
                    points. For very tiny values of C,
                    you should get misclassified examples, often even
                     if your training data is linearly separable.
    - class_weight='balanced' for unbalanced data
    - gamma: how much influence a training sample has. Larger the "gamma" is,
            the closer other examples must to be affected.
    - kernel function: "linear", "poly", "rbf"(radial bias function), sigmoid.
    - How can you avoid overfitting?
"""