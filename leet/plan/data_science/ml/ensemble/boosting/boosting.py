#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
- To reduce bias and variance
- An ensemble meta-algorithm that converts weak learners in to strong ones.
- A weak learner is highly correlated to true classification

- Iterating over weak learners and adding them to a final strong classifier.
- "Re-weighting" : Changing the weights of data points in such a way that
someway related to waek learners' accuracy.


Gradient Boosting:

- Builds the model in each iteration
- Generalizes them allowing optimization of an arbitrary differentiable loss function
- Example: Gradient Tree boosting
- Stocahastic Gradinet Boosting:
    - Sampling training data with replacement.

Gradient boosting generates learners during the learning process. It build first learner to predict the values/labels of samples, and calculate the loss (the difference between the outcome of the first learner and the real value). It will build a second learner to predict the loss after the first step. The step continues to learn the third, forth… until certain threshold.

Adaboost requires users specify a set of weak learners (alternatively,
it will randomly generate a set of weak learner before the real learning process). It will learn the weights of how to add these learners to be a strong learner. The weight of each learner is learned by whether it predicts a sample correctly or not. If a learner is mispredict a sample, the weight of the learner is reduced a bit. It will repeat such process until converge.


class sklearn.ensemble.AdaBoostClassifier(base_estimator=None,
n_estimators=50, learning_rate=1.0, algorithm='SAMME.R', random_state=None)[source]

class sklearn.ensemble.GradientBoostingClassifier(loss='deviance',
learning_rate=0.1, n_estimators=100, subsample=1.0, criterion='friedman_mse',
 min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_decrease=0.0, min_impurity_split=None, init=None, random_state=None, max_features=None, verbose=0, max_leaf_nodes=None, warm_start=False, presort='deprecated', validation_fraction=0.1, n_iter_no_change=None, tol=0.0001, ccp_alpha=0.0)[source]¶
"""