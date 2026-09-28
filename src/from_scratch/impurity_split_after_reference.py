"""
Post-reference extension of the own first attempt (commit 53a67d5).

Kept from first attempt (do not erase history):
- Gini 1 - sum(p^2)
- Midpoint thresholds between unique sorted values

Added after reading ML-From-Scratch ClassificationTree / DecisionTree._build_tree:
- min_samples: refuse a side that is too small (their min_samples_split)
- min_gain: refuse a split that barely reduces impurity (their min_impurity)
- optional entropy impurity (what their ClassificationTree actually uses)

Not copied: their DecisionNode / full recursive _build_tree.
"""

from __future__ import annotations

import numpy as np


def gini(y: np.ndarray) -> float:
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    return float(1 - np.sum(probabilities ** 2))


def entropy(y: np.ndarray) -> float:
    """Same idea as ML-From-Scratch calculate_entropy; vectorized."""
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    p = counts / len(y)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def _impurity(y: np.ndarray, kind: str) -> float:
    if kind == "gini":
        return gini(y)
    if kind == "entropy":
        return entropy(y)
    raise ValueError("kind must be 'gini' or 'entropy'")


def best_split(
    X: np.ndarray,
    y: np.ndarray,
    min_samples: int = 1,
    min_gain: float = 0.0,
    impurity: str = "gini",
):
    """
    Return (feature, threshold, gain) or (None, None, 0.0) if no legal split.

    min_samples / min_gain are pre-pruning on *this* candidate split only.
    """
    parent = _impurity(y, impurity)
    best_gain = 0.0
    best_feature = None
    best_threshold = None

    for feature in range(X.shape[1]):
        values = np.unique(X[:, feature])
        thresholds = (values[:-1] + values[1:]) / 2
        for t in thresholds:
            left = X[:, feature] < t
            right = X[:, feature] >= t
            left_y = y[left]
            right_y = y[right]
            if len(left_y) < min_samples or len(right_y) < min_samples:
                continue
            left_w = len(left_y) / len(y)
            right_w = len(right_y) / len(y)
            child = left_w * _impurity(left_y, impurity) + right_w * _impurity(
                right_y, impurity
            )
            gain = parent - child
            if gain > best_gain:
                best_gain = gain
                best_threshold = float(t)
                best_feature = int(feature)

    if best_feature is None or best_gain <= min_gain:
        return None, None, 0.0
    return best_feature, best_threshold, best_gain
