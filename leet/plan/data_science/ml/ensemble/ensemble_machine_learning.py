#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
1. Using multiple algorithms predictions to determine the output prediction of
   a sample

- Ensemble techniques:
    - Bayes Optimal classifier
        - Ensemble of hypothesis in the hypothesis space.
    - Bootstrap aggregating(bagging)
        - Each model in the ensemble with equal weight
        - To promote model variance, bagging trains each model in the
        ensemble using a randomly drawn subset of the training set.
            Example: Random Forest Regression combines random decision trees
    - Boosting
        - Incrementally building an ensemble by training each model to
        EMPHASIZE the training instances that were previous mis-classified.
            Example: Adaboost
    - Bayesian model averaging
        - Seeks to approximate the Bayes optimal classifier by sampling
        hypotheses from hypothesis space.

    - Bayesian model combination
        Bayesian model combination (BMC) is an algorithmic correction to
         Bayesian model averaging (BMA). Instead of sampling each model in
          the ensemble individually, it samples from the space of possible ensembles
    - A "bucket of models" is an ensemble technique in which a model
    selection algorithm is used to choose the best model for each problems.
    - Stacking: A combiner algorithm.
"""