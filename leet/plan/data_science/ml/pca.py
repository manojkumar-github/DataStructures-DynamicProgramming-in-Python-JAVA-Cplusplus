#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
LDA vs PCA:
LDA is superivsed transformation unlike PCA which is an unsupervised transformation.

PCA from scratch:

- Projecting low dimensional variable space to high dimensional
- A principal component is a normalized linear combination of the original
predictors in a data set. In image above, PC1 and PC2 are the principal components
- Why normalization - Performing PCA on un-normalized variables will lead to
insanely large loadings for variables with high variance.

PCA -> linear combination of variables, for each prinicipal componenet
maximum vairance is maintained.-> Each principal component tries to
explain the variance that is not explained by previous component. ->
Imp: Normalization of variables necessary - >
 How to chose n_components - Graph of Eigen values vs Factors
                           - Graph of variance vs no of componenents.

How to you select best p value?
"""