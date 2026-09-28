import numpy as np
import pandas as pd

def gini(y: np.array):
    if len(y) == 0:
        return 0
    
    _, counts = np.unique(y, return_counts=True)

    probabilities = counts / len(y)
    return 1 - np.sum(probabilities ** 2)

def best_split(X: np.array, y: np.array):
    parent_purity = gini(y)

    best_gain = 0
    best_feature = None
    best_threshold = None

    for feature in range(X.shape[1]):
        value = np.unique(X[:, feature])

        threshold = (value[:-1] + value[1:]) / 2

        for t in threshold:
            left = X[:, feature] < t
            right = X[:, feature] >= t

            left_y = y[left]
            right_y = y[right]

            if len(left_y) == 0 or len(right_y) == 0:
                continue

            left_weight = len(left_y) / len(y)
            right_weight = len(right_y) / len(y)

            child_purity = left_weight * gini(left_y) + right_weight * gini(right_y)

            gain = parent_purity - child_purity

            if gain > best_gain:
                best_gain = gain
                best_threshold = t
                best_feature = feature

    return best_feature, best_threshold
