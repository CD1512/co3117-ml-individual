"""
Dataset loading and experimental protocol for UCI HAR.

Protocol (frozen at tag `release-baseline`, 26 Sep 2026):
- Dataset: UCI Human Activity Recognition Using Smartphones
- Target: activity class (1..6)
- Split: subject-aware — no subject ID appears in more than one of train/val/test
- Primary metric: macro_f1
- Seed: 42
- Preprocess: StandardScaler fit on train only
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

import numpy as np
from sklearn.model_selection import GroupShuffleSplit
from sklearn.preprocessing import StandardScaler

SEED = 42
PRIMARY_METRIC = "macro_f1"

# Relative to repository root (co3117-ml/)
REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR_CANDIDATES = [
    REPO_ROOT / "data" / "raw" / "UCI HAR Dataset",
    REPO_ROOT / "data" / "raw" / "UCI_HAR_Dataset",
]

ACTIVITY_LABELS = {
    1: "WALKING",
    2: "WALKING_UPSTAIRS",
    3: "WALKING_DOWNSTAIRS",
    4: "SITTING",
    5: "STANDING",
    6: "LAYING",
}


@dataclass
class HarSplit:
    X_train: np.ndarray
    y_train: np.ndarray
    subjects_train: np.ndarray
    X_val: np.ndarray
    y_val: np.ndarray
    subjects_val: np.ndarray
    X_test: np.ndarray
    y_test: np.ndarray
    subjects_test: np.ndarray
    scaler: StandardScaler


def find_raw_dir() -> Path:
    for path in RAW_DIR_CANDIDATES:
        if (path / "train" / "X_train.txt").exists():
            return path
    searched = ", ".join(str(p) for p in RAW_DIR_CANDIDATES)
    raise FileNotFoundError(
        "UCI HAR not found. Download and extract under data/raw/. Tried: " + searched
    )


def _load_split_files(folder: Path, split: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    X = np.loadtxt(folder / split / f"X_{split}.txt")
    y = np.loadtxt(folder / split / f"y_{split}.txt").astype(int)
    subjects = np.loadtxt(folder / split / f"subject_{split}.txt").astype(int)
    return X, y, subjects


def load_raw_dataset() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Load all UCI HAR windows (official train + test concatenated).

    Returns
    -------
    X : (n_samples, 561)
    y : (n_samples,) activity labels in {1..6}
    subject_ids : (n_samples,) subject IDs
    """
    root = find_raw_dir()
    X_tr, y_tr, s_tr = _load_split_files(root, "train")
    X_te, y_te, s_te = _load_split_files(root, "test")
    X = np.vstack([X_tr, X_te])
    y = np.concatenate([y_tr, y_te])
    subjects = np.concatenate([s_tr, s_te])
    return X, y, subjects


def make_subject_aware_splits(
    X: np.ndarray,
    y: np.ndarray,
    subject_ids: np.ndarray,
    seed: int = SEED,
    test_size: float = 0.20,
    val_size: float = 0.20,
) -> HarSplit:
    """
    Group-aware train/val/test split by subject.

    1) Hold out ~20% of subjects as sealed test.
    2) From remaining subjects, hold out ~20% as validation.
    Same person never appears across train/val/test.
    """
    gss_test = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=seed)
    trainval_idx, test_idx = next(gss_test.split(X, y, groups=subject_ids))

    X_tv, y_tv, s_tv = X[trainval_idx], y[trainval_idx], subject_ids[trainval_idx]
    X_test, y_test, s_test = X[test_idx], y[test_idx], subject_ids[test_idx]

    # val_size is fraction of the *trainval* pool of subjects
    gss_val = GroupShuffleSplit(n_splits=1, test_size=val_size, random_state=seed)
    train_idx, val_idx = next(gss_val.split(X_tv, y_tv, groups=s_tv))

    X_train, y_train, s_train = X_tv[train_idx], y_tv[train_idx], s_tv[train_idx]
    X_val, y_val, s_val = X_tv[val_idx], y_tv[val_idx], s_tv[val_idx]

    _assert_no_subject_leakage(s_train, s_val, s_test)

    scaler = fit_preprocess_train_only(X_train)
    return HarSplit(
        X_train=scaler.transform(X_train),
        y_train=y_train,
        subjects_train=s_train,
        X_val=scaler.transform(X_val),
        y_val=y_val,
        subjects_val=s_val,
        X_test=scaler.transform(X_test),
        y_test=y_test,
        subjects_test=s_test,
        scaler=scaler,
    )


def _assert_no_subject_leakage(
    s_train: np.ndarray, s_val: np.ndarray, s_test: np.ndarray
) -> None:
    train_set, val_set, test_set = set(s_train), set(s_val), set(s_test)
    assert train_set.isdisjoint(val_set), "subject leak train/val"
    assert train_set.isdisjoint(test_set), "subject leak train/test"
    assert val_set.isdisjoint(test_set), "subject leak val/test"


def fit_preprocess_train_only(train_X: np.ndarray) -> StandardScaler:
    """Fit StandardScaler on training data only."""
    scaler = StandardScaler()
    scaler.fit(train_X)
    return scaler


def load_protocol_split(seed: int = SEED) -> HarSplit:
    """Convenience: load raw HAR and build the frozen subject-aware protocol split."""
    X, y, subjects = load_raw_dataset()
    return make_subject_aware_splits(X, y, subjects, seed=seed)


def split_summary(split: HarSplit) -> dict:
    return {
        "n_train": int(len(split.y_train)),
        "n_val": int(len(split.y_val)),
        "n_test": int(len(split.y_test)),
        "n_subjects_train": int(len(set(split.subjects_train))),
        "n_subjects_val": int(len(set(split.subjects_val))),
        "n_subjects_test": int(len(set(split.subjects_test))),
        "subjects_train": sorted(int(s) for s in set(split.subjects_train)),
        "subjects_val": sorted(int(s) for s in set(split.subjects_val)),
        "subjects_test": sorted(int(s) for s in set(split.subjects_test)),
        "seed": SEED,
        "primary_metric": PRIMARY_METRIC,
    }
