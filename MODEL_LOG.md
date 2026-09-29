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

* **Mathematical objective / decision rule:**
  My implementation is a Rosenblatt Perceptron for binary classification. It calculates the linear score \(z = w^T x + b\) and predicts \(\hat y = +1\) when \(z \ge 0\), otherwise \(\hat y = -1\). If a sample is misclassified, the update is \(w \leftarrow w + \eta yx\) and \(b \leftarrow b + \eta y\), with \(y \in \{+1,-1\}\).

* **Assumptions, inductive bias, expected failure modes:**
  The model assumes that the two classes can be separated by one linear decision boundary. Its main inductive bias is a linear boundary. A single Perceptron cannot solve non-linearly separable problems such as XOR. On HAR, the binary Rosenblatt formulation also does not directly match the six-class target, so a multi-class setup such as one-vs-rest is needed for a full six-class experiment.

* **Data representation and preprocessing:**
  Same HAR protocol as the other Part I models, using src/data.py and the 561 numeric features defined by the frozen data protocol. Labels for this binary Perceptron implementation use the \(\{+1,-1\}\) format.

* **Own pre-reference commit:**
  9660873 — src/from_scratch/perceptron_first_attempt.py

* **Reference code/notebook consulted:**
  ML-From-Scratch/mlfromscratch/supervised_learning/perceptron.py

  Reference mapping:

  1. Linear score X.dot(W) + w0 → fit, L47.
  2. Sigmoid activation → fit, L48; default Sigmoid is set in __init__, L29.
  3. Loss gradient × activation gradient → fit, L50.
  4. Weight gradient X.T.dot(error_gradient) → fit, L52.
  5. Gradient update W -= learning_rate * grad_wrt_w and w0 -= learning_rate * grad_wrt_w0 → fit, L55–56.

  Compared with my implementation, the reference file uses a Sigmoid output, an explicit loss, and gradient-based updates. My implementation uses the Rosenblatt rule with sign(z) and updates only when a sample is misclassified. The reference file is therefore closer to a one-layer neural network / Delta-rule style implementation than the classic Rosenblatt Perceptron.

* **Code-to-theory mapping (Depth A):**

  1. Linear score \(w^T x+b\) → perceptron_first_attempt.py fit L16.
  2. Sign decision rule → fit L18 (+1 if score ≥ 0 else -1).
  3. Update only when misclassified → fit L19–21.
  4. Weight update \(w \leftarrow w+\eta yx\) → fit L20.
  5. Bias update \(b \leftarrow b+\eta y\) → fit L21.
  6. Six-class OvR (meaningful modification) → perceptron_ovr.py: binary labels L19, decision_function scores + argmax in predict L31–39.

* **Hyperparameters and selection procedure:**
  Fixed for the HAR benchmark: \(\eta = 0.1\), epochs = 10 (same values as the first attempt). Not tuned on validation; one controlled comparison only. Protocol split already frozen at R0 (src/data.py, seed 42).

* **Primary/secondary metrics, runtime:**
  Primary: Macro-F1. Secondary: accuracy + confusion matrix.
  Sealed test (seed 42): own OvR Macro-F1 0.836 / accuracy 0.823 (about 0.57 s); sklearn Perceptron Macro-F1 0.862 / accuracy 0.855 (about 0.26 s). See results/perceptron_benchmark.json and results/metrics.csv.

* **One diagnostic plot/table + one focused experiment:**
  Diagnostic table: labeled confusion matrices in results/perceptron_benchmark.json (rows = true, columns = predicted; SITTING / STANDING / LAYING dominate errors).
  Focused experiment: own OvR vs sklearn Perceptron on the same HAR protocol (η=0.1, 10 epochs) via experiments/part1_pre_midterm/run_perceptron_benchmark.py. No 2-D boundary plot (none saved under results/figures/).

* **Error/limitation analysis and use-case fit:**
  Single linear boundary: XOR fails; HAR needs OvR for six classes. On this split, walking classes are mostly clean; static postures (SITTING / STANDING / LAYING) confuse each other. Own OvR trails sklearn slightly on Macro-F1 in one run — not claimed as a significant win/loss.

* **Exam-ready paragraph (no code):**
  A Perceptron is a linear binary classifier that calculates a score from the input features and predicts a class based on the sign of the score. When a sample is misclassified, it updates the weights and bias to move the decision boundary. This works when the data is linearly separable, but a single Perceptron cannot solve non-linear problems such as XOR. In contrast, the Delta rule uses the size of the prediction error and gradient descent to update the parameters. Therefore, the main difference is that the Perceptron is mistake-driven, while the Delta rule is error- and gradient-driven.


### MLP / backpropagation — Chapter 3 — Depth A

_Status: planned W06._

### Naive Bayes — Chapter 4 — Depth A

_Status: planned W07._

### Genetic Algorithm — Chapter 5 — Depth B

_Status: planned W07._

### Bayesian Network / TAN — Chapter 6 (Part I portion) — Depth C / theory

_Status: planned Part I closeout (12–14 Oct 2026)._
