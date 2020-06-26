#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
Classification Metrics:

TN:
TP:
FP: False positives - False alarm - Type 1 error
FN: False negatives - Type - 2 error

Accuracy:
    = (TP+TN)/(TP + TN + FP + FN)

Precision or Positive Predicted Value:
    Precision = TP / (TP + FP)
              = ((relevant_documents) ^ (retrieved_documents))/(
              retireved_documents)
              = number of correct results/ number of all returned results

Recall(Sensitivity, Hit-rate, True-Positive-rate):
    Recall = TP / (TP + FN)
           = (relevant_documents) ^ (retrieved_documents))/
             (relevant_documents)
           = number of correct results/number of results that should have
           been returned.

Miss rate or False Negative Rate(FNR):
    FNR = 1 - TPR = FN/(FN + TP)

Specificity(Selectivity or True-Negative-rate)
    TNR = TN/(TN + FP) = 1 - FPR

False Positive Rate (FPR):
    FPR = FP/(FP+ TN)

F1 Score: Harmonic mean of precision and recall
        F1= 2 (Precision * Recall)/(Precision + Recall)

Confusion Matrix:
    - n*n 2D table of model predictions and true-predictions

ROC:
    - Receiver Operating characteristic curve shows the performance of a
    binary classifier as function of its cut-off threshold.
    - TPR vs FPR for the various threshold values.
    - Similar to our cut-point MTSs
    - Pick a threshold such that a trade-off is arrived between PRECISION and
      RECALL
    - Used for probabilistic outputs
    - Plot and see the model performances

AUC:
    - Area under the curve (AUC)
    - Aggregate measure of a binary classifier on all possible threshold values
    - Threshold invariant
    - Computes the area under ROC curve
    - AUC is as the probability that the model ranks a random positive
        example more highly than a random negative example
    - Higher the AUC the better the model is

Gini Cofficient:
    - Ratio
    - (Area between ROC curve and the diagnol line)/ Area above triangle
    - 2 * AUC - 1
    - Purpose: To normalize the AUC

Regression metrics:

MSE: Mean Squared Error
    - Avg squared error between expected and predicted values.

MAE:
    - No squaring
    - Just absolute difference between expected and predicted values.

RMSE
    - Root Mean Squared Error
    - Square root of MSE

R^2:
    - 1- (MSE(model) - MSE(baseline))

Other metrics:


Jaccard Index:
    - Size of intersection / Size of Union

p-value:
    - Probability of obtaining observed results of the test assuming that
    null hypothesis is correct
    - Level of marginal siginificance within stasticical
    hypothesis test Probability of occurence of a given
    event
    - p-values are calculated spreadsheets/stastical software

t-value
    - Size of the variation relative to the variation in data
    - greater the t-value, greater the evidence against the null hypothesis.


a/b-test
    - randomized experiment with two variants A and B.
    - Two sample hypothesis testing
    - Compare two versions of a single variable
    - Example: A/B testing on a website: Randomly serving visitors two versions
    of a website that differ only in the design of single button,
    the relative efficiencies of two designs can be measured.

Pearson - Correlation:
    - [-1, 1]


Cophen Kappa Score:
    - Inter Annotator Agreement

QWK:
    - changed adjusted indexed agreements.
    - amount of agreement of algorithimic predictions

"""