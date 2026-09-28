# MODEL_LOG.md — per-model records

One section per model family. Fill each item from assignment §9.1 after the corresponding week.

Template (copy for each model):

```
## [Model name] — Chapter X — Depth A/B/C

- Mathematical objective / factorization / decision rule:
- Assumptions, inductive bias, expected failure modes:
- Data representation and preprocessing:
- Own pre-reference commit:
- Reference code/notebook consulted:
- Hyperparameters and selection procedure:
- Primary/secondary metrics, runtime:
- One diagnostic plot/table + one focused experiment:
- Error/limitation analysis and use-case fit:
- Exam-ready paragraph (no code):
```

---

## Models (Part I)

### Decision Tree — Chapter 2 — Depth B (release catch-up)

- Mathematical objective / factorization / decision rule: choose the feature/threshold that maximises impurity decrease (Gini first attempt; entropy in ML-From-Scratch ClassificationTree).
- Assumptions, inductive bias, expected failure modes: axis-aligned splits; greedy (no look-ahead); high-variance if grown unpruned.
- Data representation and preprocessing: same HAR protocol (`src/data.py`), 561 numeric features.
- Own pre-reference commit: `53a67d5` `src/from_scratch/impurity_split_first_attempt.py`
- Reference code/notebook consulted: ML-From-Scratch `decision_tree.py` `_build_tree` L72–134, `_calculate_information_gain` L257–265; `calculate_entropy`; `divide_on_feature`.
- Code-to-theory mapping (Depth B, ≥3 steps):
  1. Gini impurity → `impurity_split_first_attempt.py` `gini()` L3–11. Reference counterpart: `calculate_entropy` (ClassificationTree uses entropy, not Gini).
  2. Weighted information gain → `best_split()` L34–40. Reference: `_calculate_information_gain` L257–265.
  3. Midpoint thresholds between unique sorted values → `best_split()` L20–23. Reference: `divide_on_feature` uses raw unique values as cut points.
  4. Stopping knobs after reference → `impurity_split_after_reference.py` `min_samples` L72, `min_gain` L85. Reference: `_build_tree` `min_samples_split` / `min_impurity`.
- Hyperparameters and selection procedure: sklearn compare only — unconstrained vs `max_depth=6, min_samples_leaf=20` vs `ccp_alpha=0.002` on sealed test.
- Primary/secondary metrics, runtime: see `results/dt_stop_vs_prune.json` / `results/metrics.csv`
- One diagnostic plot/table + one focused experiment: stopping vs post-pruning leaf/depth vs Macro-F1 on same split (`experiments/part1_pre_midterm/run_dt_stop_vs_prune.py`).
- Error/limitation analysis and use-case fit: catch-up implements split logic, not a full from-scratch tree; HAR features are already engineered so a deep tree can overfit subjects even with group split.
- Exam-ready paragraph (no code): A decision tree picks the cut that most reduces label mix at a node (information gain). Growing until train is pure memorizes noise; stopping during growth or pruning afterwards trades a little train fit for better generalization.

### Perceptron / Delta — Chapter 3 — Depth A

_Status: not started (planned end of W05)._

### MLP / backpropagation — Chapter 3 — Depth A

_Status: planned W06._

### Naive Bayes — Chapter 4 — Depth A

_Status: planned W07._

### Genetic Algorithm — Chapter 5 — Depth B

_Status: planned W07._

### Bayesian Network / TAN — Chapter 6 (Part I portion) — Depth C / theory

_Status: planned Part I closeout (12–14 Oct 2026)._
