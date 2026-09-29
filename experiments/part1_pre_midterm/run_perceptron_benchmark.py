"""Own OvR perceptron vs sklearn on the frozen HAR protocol (seed 42)."""

from __future__ import annotations

import csv
import json
import sys
import time
from pathlib import Path

from sklearn.linear_model import Perceptron as SklearnPerceptron

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.data import ACTIVITY_LABELS, load_protocol_split  # noqa: E402
from src.from_scratch.perceptron_ovr import OneVsRestPerceptron  # noqa: E402
from src.metrics import summarize_classification  # noqa: E402

ETA = 0.1
EPOCHS = 10
CLASS_ORDER = list(range(1, 7))
CLASS_NAMES = [ACTIVITY_LABELS[c] for c in CLASS_ORDER]


def labeled_confusion(cm) -> dict:
    """rows = true label, columns = predicted; order = CLASS_NAMES."""
    return {"labels": CLASS_NAMES, "matrix": cm.tolist()}


def eval_on_test(name, predict, split, runtime):
    m = summarize_classification(split.y_test, predict)
    print(
        f"{name}: macro_f1={m['macro_f1']:.4f} acc={m['accuracy']:.4f} "
        f"runtime={runtime:.2f}s"
    )
    return {
        "model": name,
        "macro_f1": float(m["macro_f1"]),
        "accuracy": float(m["accuracy"]),
        "runtime_seconds": runtime,
        "confusion_matrix": labeled_confusion(m["confusion_matrix"]),
    }


def main() -> None:
    split = load_protocol_split()

    t0 = time.perf_counter()
    own = OneVsRestPerceptron(learning_rate=ETA, epochs=EPOCHS)
    own.fit(split.X_train, split.y_train)
    own_row = eval_on_test(
        "perceptron_ovr", own.predict(split.X_test), split, time.perf_counter() - t0
    )

    t0 = time.perf_counter()
    sk = SklearnPerceptron(
        random_state=42,
        max_iter=EPOCHS,
        eta0=ETA,
        tol=None,
        shuffle=False,
    )
    sk.fit(split.X_train, split.y_train)
    sk_row = eval_on_test(
        "sklearn_perceptron",
        sk.predict(split.X_test),
        split,
        time.perf_counter() - t0,
    )

    rows = [own_row, sk_row]
    out = ROOT / "results" / "perceptron_benchmark.json"
    payload = {
        "week": "W05",
        "split": "test",
        "seed": 42,
        "eta": ETA,
        "epochs": EPOCHS,
        "confusion_matrix_note": "rows = true label, columns = predicted label; class order 1..6",
        "class_labels": {str(c): ACTIVITY_LABELS[c] for c in CLASS_ORDER},
        "rows": rows,
    }
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")

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
                    f"seed=42; eta={ETA}; epochs={EPOCHS}",
                ]
            )
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
