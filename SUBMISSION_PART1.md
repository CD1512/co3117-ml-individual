# SUBMISSION_PART1.md

**Status:** stub — fill before tag `part1-final` on 14 Oct 2026.

Part I portfolio index. Instructor should verify progress via [PROGRESS.md](PROGRESS.md) in under two minutes.

## Checklist (assignment §10)

| Item | Path / evidence | Done |
| :---- | :---- | :---- |
| W01–W04 catch-up post | `docs/pre-release/PRE_RELEASE_CATCHUP.md` | [x] |
| Release baseline diagnostic | `exercises/release-baseline-w01-w04.pdf` (`4ab63ec`) | [x] |
| Decision Tree catch-up (Depth B) | `impurity_split_first_attempt.py` (`53a67d5`) then `impurity_split_after_reference.py` + stop/prune (`490e7b4`); mapping in MODEL_LOG + post C | [x] |
| Tag `release-baseline` | Git tag on the catch-up freeze commit | [x] |
| W05 Perceptron + post + drill + `w05` | links TBD | [ ] |
| W06 MLP + grad check + `w06` | links TBD | [ ] |
| W07 Naive Bayes + GA + `w07` | links TBD | [ ] |
| BN/TAN Part I theory | notes + post | [ ] |
| Frozen protocol (split/metric/seed) | `src/data.py`, `data/README.md` (seed 42, Macro-F1, subject-aware) | [x] |
| `part1_summary.pdf` | `report/part1_summary.pdf` | [ ] |
| `a4-notes-part1-midterm.pdf` | `exam/a4-notes-part1-midterm.pdf` | [ ] |
| Tag `part1-final` | Git tag on 14 Oct 2026 | [ ] |

## How to reproduce (fill at freeze)

```bash
python -m venv .venv
# activate, then:
pip install -r requirements.txt
python experiments/part1_pre_midterm/run_majority_baseline.py
python experiments/part1_pre_midterm/run_dt_stop_vs_prune.py
```

Requires a local copy of UCI HAR under `data/raw/` (gitignored). See `data/README.md`.

## AI disclosure

See [AI_USE.md](AI_USE.md).
