#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
- Supervised algorithm
- For classification and regression
- Selection of the most significant variable that gives the most
    homogeneous population
- Types:
    - Categorical Variable Decision Tree
    - Continuous Variable Decision Tree
- Pruning:
    - Removing the sub-nodes (opposite to splitting)
- Non parametric method

Disadvantages:
    - Overfitting
    - Not fit for continous variables
- Regression: Mean value of observations falling in the region
- Classification tree: mode of observations

How does tree know where to split?::
    - Does all the splits and picks that split which gives most homogenous
    sub-nodes
        - Gini-impurity = 1- Gini
        - Chi-Square that finds out stasticial significance.
        - Information Gain vs Entropy:
            - If sample is compeletely homogeneous, then the entropy is zero.
            - if the sample is equally divided as 50%-50% then the entropy
            is one.
            Entropy =  -plog2(p) - q(log2q)
            Information gain = 1- Entropy
        - Reduction in Variance (For Regression Tree)
            - Select the split with lower variance.

How to avoid over-fitting in decision tree?
    - Setting constraints on tree size
    - Tree pruning

    Some useful parameters to tune:
        - Minimum samples for a node split
        - Minimum samples for a tree node
        - Maximum depth of tree
        - Maximum number of terminal nodes
        - Maximum features to consider for the split.
        - Pruning

When to use?

- If the relationship between dependent & independent variable is well
approximated by a linear model, linear regression will outperform tree based model.
- If there is a high non-linearity & complex relationship between dependent &
independent variables, a tree model will outperform a classical regression method.
- If you need to build a model which is easy to explain to people, a decision
tree model will always do better than a linear model. Decision tree models
are even simpler to interpret than linear regression!


class sklearn.tree.DecisionTreeClassifier(criterion='gini', splitter='best',
 max_depth=None, min_samples_split=2, min_samples_leaf=1,
 min_weight_fraction_leaf=0.0, max_features=None, random_state=None,
 max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None,
  class_weight=None, presort='deprecated', ccp_alpha=0.0
"""