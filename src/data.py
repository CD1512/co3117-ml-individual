"""
Dataset loading and experimental protocol.

DRAFT until R0 freeze (tag `release-baseline`).
Do not claim a frozen split/metric/seed until catch-up is complete and values
are pinned here and in data/README.md.
"""

from __future__ import annotations

# Draft seed — confirm at R0
SEED = 42

# Draft primary metric name (implementation in metrics.py)
PRIMARY_METRIC = "macro_f1"


def load_raw_dataset():
    """Load UCI HAR (or approved alternative). Not implemented yet — planned 25 Sep."""
    raise NotImplementedError("Download and load UCI HAR; see data/README.md")


def make_subject_aware_splits(X, y, subject_ids, seed: int = SEED):
    """
    Group-aware train/val/test split by subject.

    TODO: implement with GroupShuffleSplit / GroupKFold so the same person
    never appears in both train and test.
    """
    raise NotImplementedError("Subject-aware split — implement at R0 data day")


def fit_preprocess_train_only(train_X):
    """Fit scalers/encoders on training data only; return fitted transformers."""
    raise NotImplementedError("Preprocess fit on train only")
