"""
Evaluation helpers for the fixed experimental protocol.

Primary metric (draft until R0): Macro-F1 for multiclass classification.
Always report accuracy and a confusion matrix as secondary evidence.
"""

from __future__ import annotations

from typing import Any

import numpy as np


def macro_f1(y_true, y_pred) -> float:
    """Compute macro-averaged F1. Thin wrapper — prefer sklearn in callers for now."""
    from sklearn.metrics import f1_score

    return float(f1_score(y_true, y_pred, average="macro", zero_division=0))


def accuracy(y_true, y_pred) -> float:
    from sklearn.metrics import accuracy_score

    return float(accuracy_score(y_true, y_pred))


def confusion(y_true, y_pred) -> Any:
    from sklearn.metrics import confusion_matrix

    return confusion_matrix(y_true, y_pred)


def summarize_classification(y_true, y_pred) -> dict[str, Any]:
    """Return the standard secondary bundle for MODEL_LOG / results."""
    return {
        "macro_f1": macro_f1(y_true, y_pred),
        "accuracy": accuracy(y_true, y_pred),
        "confusion_matrix": confusion(y_true, y_pred),
    }


def majority_baseline_predict(y_train: np.ndarray, n_test: int) -> np.ndarray:
    """Simple baseline: predict the most frequent training label for all test rows."""
    values, counts = np.unique(y_train, return_counts=True)
    majority = values[np.argmax(counts)]
    return np.full(n_test, majority)
