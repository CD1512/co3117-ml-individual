"""
Catch-up experiment: pre-pruning (stopping) vs post-pruning on the *same*
subject-aware HAR protocol. Uses sklearn trees as the full-tree engine;
own code remains the impurity/split study, not a from-scratch forest.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from sklearn.tree import DecisionTreeClassifier

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.data import load_protocol_split  # noqa: E402
from src.metrics import summarize_classification  # noqa: E402


def eval_tree(name: str, clf: DecisionTreeClassifier, split) -> dict:
    clf.fit(split.X_train, split.y_train)
    pred = clf.predict(split.X_test)
    m = summarize_classification(split.y_test, pred)
    row = {
        "model": name,
        "macro_f1": m["macro_f1"],
        "accuracy": m["accuracy"],
        "n_leaves": int(clf.get_n_leaves()),
        "depth": int(clf.get_depth()),
    }
    print(
        f"{name}: macro_f1={row['macro_f1']:.4f} acc={row['accuracy']:.4f} "
        f"leaves={row['n_leaves']} depth={row['depth']}"
    )
    return row


def main() -> None:
    split = load_protocol_split()
    rows = [
        eval_tree(
            "dt_unconstrained",
            DecisionTreeClassifier(random_state=42),
            split,
        ),
        eval_tree(
            "dt_preprune_max_depth_6",
            DecisionTreeClassifier(max_depth=6, min_samples_leaf=20, random_state=42),
            split,
        ),
        eval_tree(
            "dt_postprune_ccp_alpha",
            DecisionTreeClassifier(ccp_alpha=0.002, random_state=42),
            split,
        ),
    ]

    out = ROOT / "results" / "dt_stop_vs_prune.json"
    out.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    metrics = ROOT / "results" / "metrics.csv"
    with metrics.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for r in rows:
            w.writerow(
                [
                    "W05",
                    r["model"],
                    "test",
                    f"{r['macro_f1']:.6f}",
                    f"{r['accuracy']:.6f}",
                    f"leaves={r['n_leaves']}; depth={r['depth']}; seed=42",
                ]
            )
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
