#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
Bagging(also known as bootstrap aggregating):
    - Combining the result of multiple classifiers on different sub-samples
    of the same data set.
    - 1. Create multiple datasets
      2. Create multiple models
      3. Combine models. (using mean meadian mode)

Random Forest: (bagging of Decision trees)
- Random training dataset samples with replacement.
- Aggregate the predicitions of the decision trees

class sklearn.ensemble.RandomForestClassifier(n_estimators=100,
criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1,
min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,
min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=True,
oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False,
class_weight=None, ccp_alpha=0.0, max_samples=None
"""