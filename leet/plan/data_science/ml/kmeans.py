#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
- Centriod based algorithm or a distance based algorithm
- In k-means each cluster has a centroid
- Objective: Minimize the sum of the distances between the points and their
            respective cluster centroid
- Algorithm:
    - Choose the number of clusters "k"
    - Select "k" random points as centriods from the data.
    - Move(assign) all points to each of the closest centroid
    - Recompute the centroids of newly formed clusters.
    - Repeat step 3 and step 4
    - Stopping Criteria:
        - Centroids of newly formed clusters do not change.
        - Points remain in the same cluster.
        - Maximum number of interations reached.

- How do you select best k?
    - Elbow Rule: Cluster vs Intertia value.
"""