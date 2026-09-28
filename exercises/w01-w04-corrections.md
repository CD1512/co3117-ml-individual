# Corrections — W01–W04 release baseline diagnostic

Assignment §7.1: first-attempt PDF is left unchanged. This Markdown is the
corrected version after checking notes/textbooks/MOOC. Each item: what the
paper said, what was wrong or missing, the correction, and a cited source.

- First attempt (do not edit): exercises/release-baseline-w01-w04.pdf
  (handwritten, Tran Chi Dai, dated 25/09/2026 on the scan)
- English transcript used only to read the paper: workspace file
  "chuyen sang tieng anh het cho toi nhe.md" (not an extra first attempt)
- Corrections written: 28/09/2026
- Linked catch-up post: docs/pre-release/PRE_RELEASE_CATCHUP.md

---

## Machine learning foundations

### Supervised learning

- First attempt: trained on labeled data to learn a mapping from inputs to outputs.
- After check: correct. No change.
- Source: CO3117 notes, Chapter 1; Mitchell (1997), Machine Learning, Ch. 1
  (learning from labeled examples).

### Train / validation / test

- First attempt: train fits parameters; validation tunes hyperparameters, picks
  a checkpoint, and watches overfitting; test stays sealed until selection is
  frozen, then measures generalization.
- After check: the split roles are correct. Missing: validation can also be used
  for early stopping. Missing the leakage rule for preprocessing (see next item).
- Correction: fit the model on train only; use validation to choose
  hyperparameters and when to stop; evaluate the frozen choice once on test.
- Source: Müller and Guido (2017), Introduction to Machine Learning with Python,
  Ch. 5 (model evaluation and improvement); NPTEL IIT Madras, Introduction to
  Machine Learning, Week 7 (evaluation / cross-validation); assignment §2 and §9
  (sealed test, fit preprocess on train only).

### Data leakage (not written as its own answer on the PDF)

- First attempt: said the test set is sealed for final evaluation, but did not
  say that fitting a scaler or choosing hyperparameters on test is leakage.
- After check: this is a gap vs the W01–W04 baseline prompt (leakage checklist).
- Correction: never fit a scaler, encoder, or search hyperparameters on test.
  Fit those steps on train, then transform val/test. Using test for those steps
  makes the score look better than true generalization.
- Source: assignment §2 and §9; Müller and Guido (2017), Ch. 4–5 (preprocessing
  and evaluation pipelines). Linked later experiment protocol: src/data.py
  (StandardScaler fit on train only).

### Underfitting and overfitting

- First attempt: underfitting = too simple to capture structure; overfitting =
  too complex and memorizes noise on train. The learning-curve sketch then gave
  the error pattern (simple: both errors high and close; complex: train near
  zero, val down then up).
- After check: definitions are correct. The paper did not write the usual
  train-vs-val table in the underfitting/overfitting bullet itself, but the
  curve paragraph covers it. Small extra: overfitting does not require train
  error exactly zero — a large gap (low train error, high val error) is enough.
- Source: Müller and Guido (2017), Ch. 2 (generalization, overfitting);
  NPTEL Weeks 0–1 (bias–variance / overfitting). Catch-up post section A.

### Bias and variance

- First attempt: high bias = underfitting, cannot learn the pattern on train
  and test; high variance = too sensitive to small fluctuations and noise in
  the training set.
- After check: direction is correct (bias ~ underfit, variance ~ overfit).
  Tighten: high bias means the hypothesis is too rigid, so error stays high on
  train and on new data. High variance means the fit jumps when the training
  sample changes, so train can look good while new data is much worse.
- Source: NPTEL Weeks 0–1; CO3117 notes, Chapter 1 (bias–variance).

### Learning curve (complexity on the x-axis)

- First attempt: too simple → train and val errors high and close; too complex
  → train error near zero, val error falls then rises.
- After check: correct for x = model complexity. The prompt also allows
  x = training set size. That picture is different: more data often reduces
  variance (val error drops, the gap shrinks); more data barely helps high
  bias — the model family is still too weak.
- Source: Müller and Guido (2017), Ch. 5 (learning curves); NPTEL Week 7.

---

## Decision Trees

### Impurity

- First attempt: impurity measures how labels are distributed in a node; a node
  with one class is a “clear” (pure) node.
- After check: idea is correct. Add: impurity is high when classes are mixed in
  similar proportions; impurity is 0 when the node is pure. Gini is
  1 − sum(p_k^2); entropy is −sum(p_k log2 p_k). The first-attempt code used
  Gini (commit 53a67d5).
- Source: Mitchell (1997), Ch. 3 (decision tree learning, impurity / entropy);
  NPTEL Week 6 (decision trees). Own code:
  src/from_scratch/impurity_split_first_attempt.py, gini().

### Information gain

- First attempt: gain is the reduction in impurity after partitioning.
- After check: correct as a sentence, but the paper did not write the weighted
  average of children. Correction:

  Gain = impurity(parent) − [ (n_left / n) * impurity(left)
                              + (n_right / n) * impurity(right) ]

  Larger gain means a more useful split. The PDF also has no 4-row numerical
  example (Sunny/Rain). A tiny check: 2 No on Sunny and 2 Yes on Rain makes
  both children pure, so child impurity is 0 and gain is maximal for that
  parent.
- Source: Mitchell (1997), Ch. 3 (information gain); NPTEL Week 6.
  Catch-up post section B (the Sunny/Rain example, done after the PDF).

### Continuous attributes

- First attempt: sort values, try thresholds between adjacent values, binary
  split, pick the threshold with largest information gain.
- After check: correct. Convention: left if x < c, right if x >= c (or ≤ / >).
  Midpoints between unique sorted values are the usual candidates. This matches
  the later first-attempt split code (midpoints), which differs from
  ML-From-Scratch using raw unique values as thresholds.
- Source: Mitchell (1997), Ch. 3 (continuous attributes); mapping in
  MODEL_LOG.md (Decision Tree mapping).

### Missing values

- First attempt: mean/median imputation on continuous features, computed from
  the training set.
- After check: this is one valid, simple method and it respects train-only
  fitting. It is not the only tree-specific method. Alternatives (not required
  to derive on the diagnostic): treat missing as its own category; C4.5 sends a
  fraction of the instance down each branch using frequencies of known values.
  I did not write those on the PDF — left as a knowledge gap, not a wrong
  answer.
- Source: Mitchell (1997), Ch. 3 (missing attribute values); Müller and Guido
  (2017), Ch. 4 (imputation). Catch-up post section G.

### Pre-pruning vs post-pruning

- First attempt: pre-pruning stops growth when a stopping rule is met;
  post-pruning grows until leaves are pure, then evaluates and removes later.
- After check: the contrast is correct. Add purpose: both limit complexity to
  reduce overfitting. Pre-pruning examples: max depth, min samples in a node,
  min gain. Post-pruning example: cost-complexity pruning, choose alpha on
  validation (R_alpha(T) = R(T) + alpha * |T|). I did not write the alpha
  formula on the paper; that remains a gap.
- Source: Mitchell (1997), Ch. 3 (avoiding overfitting: stopping and pruning);
  sklearn DecisionTreeClassifier (max_depth, min_samples_leaf vs ccp_alpha).
  Same-split experiment: results/dt_stop_vs_prune.json and catch-up post
  section D (unconstrained vs max_depth=6 vs ccp_alpha).

---

## Knowledge gaps (things the PDF did not cover)

1. Leakage wording: scaler / hyperparameter search must not use test.
2. Information-gain formula with child weights; no hand calculation on paper.
3. C4.5-style missing-value split (fractional instances).
4. Cost-complexity alpha: how it is chosen on validation.

These are filled here and in the catch-up post (B, D, G), not by editing the PDF.

---

## Sources used for this file (assignment §7.1 cite requirement)

1. CO3117 notes, Chapters 1–2.
2. Assignment spec §2, §7.1, §9.
3. Tom Mitchell (1997), Machine Learning, Ch. 1 and Ch. 3.
4. Müller and Guido (2017), Introduction to Machine Learning with Python,
   Ch. 2, 4, 5.
5. NPTEL, Ravindran, Introduction to Machine Learning: Weeks 0–1, 6, 7.
6. Own later artifacts (not used to rewrite the PDF): commit 53a67d5;
   docs/pre-release/PRE_RELEASE_CATCHUP.md; results/dt_stop_vs_prune.json.
