#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
Why Naive? (Assumaptions that all variables of the data are independent)

Bayes Theorem:

P(A/B) = (P(B/A) * P(A)) / P(B)

P(class/data) = (P(data/class) P(class)) /P(data)

class = is a particular class
data = is an observation's data
p(class|data) is called posterior
p(data|class) is likelihood
p(class) is called the prior
p(data) is marginal probability

Implementation: https://chrisalbon.com/machine_learning/naive_bayes/naive_bayes_classifier_from_scratch/

class sklearn.naive_bayes.GaussianNB(priors=None, var_smoothing=1e-09)


"""