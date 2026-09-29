# Corrections — W05 handwritten drill (Perceptron / Delta)

Assignment §7.1: the first-attempt PDF is left unchanged. This Markdown is
the corrected version after checking notes/textbooks/MOOC. Each item: what
the paper said, what was wrong or missing, the correction, and a cited source.

- First attempt (do not edit): exercises/w05-first-attempt.pdf
  (handwritten, dated 28/09/2026 on the scan)
- Code first attempt (same commit): src/from_scratch/perceptron_first_attempt.py
- Corrections written: 28/09/2026

---

## (A) Perceptron update

- First attempt (PDF): a perceptron is a linear classifier/function; score
  z = w^T x + b; when misclassified, w <- w + η y x and b <- b + η y x
  (the bias update includes x in the first attempt). η = learning rate.
- After check: partly correct. The score and weight update are correct, but
  the bias update is wrong. The bias update should be b <- b + η y, without x.
- Correction: The Perceptron first calculates z = w^T x + b and uses the sign
  of z to get the predicted class. With y ∈ {+1, −1}, the update is only
  needed when the sample is misclassified:

  w <- w + η y x

  b <- b + η y

  If the sample is already classified correctly, there is no update.
  Geometrically, changing w changes the direction of the decision boundary,
  while changing b shifts its position.
- Source: NPTEL, Introduction to Machine Learning, Week 4 — “Separating
  Hyperplane Approaches - Perceptron Learning”; Tom M. Mitchell (1997),
  Machine Learning, Ch. 4, §4.4.2 The Perceptron Training Rule.

---

## (B) Linear separability

- First attempt (PDF): a dataset is linearly separable if a single linear
  line can separate the data into the correct classes.
- After check: the idea is correct, but “line” is only for a 2-D example. In
  higher dimensions, the separator is a hyperplane.
- Correction: A dataset is linearly separable if one linear decision boundary
  can separate the two classes, with the classes lying on different sides of
  the boundary. In 2-D, the boundary is a line. In higher dimensions, it is a
  hyperplane. For linearly separable training data, the Perceptron can
  converge to a separating weight vector after a finite number of updates.
- Source: NPTEL, Introduction to Machine Learning, Week 4 — “Separating
  Hyperplane Approaches - Perceptron Learning”; Mitchell (1997), Ch. 4,
  §4.4.1 Representational Power of Perceptrons and §4.4.2 The Perceptron
  Training Rule.

---

## (C) Why XOR fails

- First attempt (PDF): XOR is not linearly separable; positives and negatives
  cannot be classified with one straight line.
- After check: the main idea is correct. The missing point is that a single
  Perceptron can only create one linear decision boundary, while XOR cannot
  be separated by one such boundary.
- Correction: XOR has four points: (0,0) -> −, (0,1) -> +, (1,0) -> +,
  (1,1) -> −. The positive and negative points cannot be separated by one
  straight line. Therefore, a single Perceptron cannot solve XOR. The problem
  is the linear limitation of the model, not simply the learning rate or the
  number of training epochs.
- Source: NPTEL, Introduction to Machine Learning, Week 4 — “Separating
  Hyperplane Approaches - Perceptron Learning”; Mitchell (1997), Ch. 4,
  §4.4.1 Representational Power of Perceptrons.

---

## (D) Perceptron vs delta / gradient learning

- First attempt (PDF): perceptron updates when the class is misclassified;
  delta uses the magnitude of prediction error and updates through a gradient.
- After check: the idea is correct, but the difference should be stated more
  clearly. The Perceptron uses the thresholded class output, while the Delta
  rule uses the error of the unthresholded linear output.
- Correction: The Perceptron learning rule updates the weights when the
  current training example is misclassified. If the example is already
  classified correctly, there is no update.

  The Delta rule uses the prediction error of a linear unit and applies
  gradient descent to reduce the error. Therefore, the two rules look similar
  but use different outputs when calculating the update:

  Perceptron → uses the thresholded output

  Delta rule → uses the unthresholded linear output

  In simple words, the Perceptron is mainly mistake-driven, while the Delta
  rule is error- and gradient-driven. A single linear unit trained with the
  Delta rule is still linear, so the learning rule alone does not make it able
  to solve XOR.
- Source: Mitchell (1997), Ch. 4, §4.4.2 The Perceptron Training Rule and
  §4.4.3 Gradient Descent and the Delta Rule.

---

## Knowledge gaps (PDF did not cover / too thin)

1. I did not clearly connect the Perceptron update to geometry. In particular,
   I did not explain that the weight vector controls the orientation of the
   decision boundary, while the bias shifts its position.
2. I did not clearly explain why XOR fails. I only stated that XOR is not
   linearly separable, but I did not connect this to the fact that a single
   Perceptron can only create one linear decision boundary.

These stay here and in the weekly post later. Do not edit the PDF.

---

## Code first attempt (same commit `9660873`)

Do not edit `src/from_scratch/perceptron_first_attempt.py`. The checked
implementation is a new file: `src/from_scratch/perceptron_after_check.py`.

- First attempt: Rosenblatt loop is present: score `z = w·x + b`, predict
  `sign(z)`, update only when `y_pred != y_i` with `w += η y x` and
  `b += η y`. That matches Mitchell §4.4.2 and the **corrected** bias
  formula (the PDF had `b ← η y x`; the first-attempt **code** already used
  `b += η y`).
- After check: the update rule is right, but the class has two bookkeeping
  bugs: `__init__` stores `self.weight` while `fit` uses `self.weights`;
  the learning-rate name is misspelled `learing_rate`. Labels must be
  `{+1, −1}`; HAR activity ids `{1..6}` cannot be passed in unchanged.
- Correction: keep the same update; spell `learning_rate`; use one weights
  vector; document the `±1` label convention. See
  `perceptron_after_check.py`. This is not a copy of ML-From-Scratch
  `perceptron.py` (that file is sigmoid + gradient, i.e. closer to the
  delta rule in Mitchell §4.4.3).
- Source: own first-attempt file; Mitchell (1997), §4.4.2; assignment §4
  (do not erase the first attempt).

---

## Sources used for this file (§7.1 cite requirement)

List only what was actually opened:

1. NPTEL, Introduction to Machine Learning (IIT Madras), Week 4 — “Separating
   Hyperplane Approaches - Perceptron Learning.”
2. Tom M. Mitchell (1997), Machine Learning, Chapter 4 Artificial Neural
   Networks, §4.4 Perceptrons, especially:
   - §4.4.1 Representational Power of Perceptrons
   - §4.4.2 The Perceptron Training Rule
   - §4.4.3 Gradient Descent and the Delta Rule
