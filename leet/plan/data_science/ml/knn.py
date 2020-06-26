#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
- Supervised Learning Algorithm
- Instance based learning and lazy learning
- Classification and Regression
-

Ref: https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/


Algorithm:
1. Load the data
2. Initialise the value of k
3. For getting the predicted class, iterate from 1 to total number of training data points
    a) Calculate the distance between test data and each row of training data. Here we
        will use Euclidean distance as our distance metric since its the
        most popular method.The other metrics that can be used are Chebyshev,
        cosine, etc.
    b) Sort the calculated distances in ascending order based on distance
    values
    c) Get top k rows from the sorted array
    d) Get the most frequent class of these rows
    e) Return the predicted class

How to choose best value of k?
    - Change the k value and compute the validation errors.

- For knn regression take mean of predictions of neighbors
"""