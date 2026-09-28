"""Run majority-class baseline under the frozen subject-aware protocol."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.data import load_protocol_split, split_summary  # noqa: E402
from src.metrics import majority_baseline_predict, summarize_classification  # noqa: E402


def main() -> None:
    split = load_protocol_split()
    summary = split_summary(split)
    print("protocol:", json.dumps(summary, indent=2))

    y_pred = majority_baseline_predict(split.y_train, len(split.y_test))
    metrics = summarize_classification(split.y_test, y_pred)
    print(
        f"majority baseline on sealed test: "
        f"macro_f1={metrics['macro_f1']:.4f} accuracy={metrics['accuracy']:.4f}"
    )
    print("confusion_matrix:\n", metrics["confusion_matrix"])

    results_dir = ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    metrics_path = results_dir / "metrics.csv"
    write_header = not metrics_path.exists() or metrics_path.stat().st_size == 0
    with metrics_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(
                ["week", "model", "split", "macro_f1", "accuracy", "notes"]
            )
        writer.writerow(
            [
                "W05",
                "majority_baseline",
                "test",
                f"{metrics['macro_f1']:.6f}",
                f"{metrics['accuracy']:.6f}",
                f"seed=42; subjects_test={summary['subjects_test']}",
            ]
        )

    fig_meta = results_dir / "majority_baseline_summary.json"
    fig_meta.write_text(
        json.dumps(
            {
                "protocol": summary,
                "macro_f1": metrics["macro_f1"],
                "accuracy": metrics["accuracy"],
                "confusion_matrix": metrics["confusion_matrix"].tolist(),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {metrics_path}")
    print(f"wrote {fig_meta}")


if __name__ == "__main__":
    main()
