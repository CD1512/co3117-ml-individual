# CO3117 — W05 Perceptron / Delta

Author: Tran Chi Dai
Date: 29/09/2026

## A. Concept capsule

A Perceptron is a linear binary classifier. It calculates a score from the input features, weights, and bias, then predicts either +1 or -1 based on the sign of the score. It updates the weights and bias only when a sample is misclassified. The update uses the learning rate, the true label, and the current sample. The main assumption is that the classes can be separated by one linear decision boundary. The weight vector controls the direction of the boundary, while the bias shifts its position. Since HAR has 6 classes, the binary Perceptron cannot use labels 1 to 6 directly, so I use One-vs-Rest.

## B. One derivation / worked example

When a sample is misclassified, the Perceptron changes the weights and bias using the current sample and true label. This moves the decision boundary to give the wrong sample a better score. Reference: exercises/w05-first-attempt.pdf.

## C. Code-to-theory

My perceptron_first_attempt.py calculates the linear score in fit around L16. Around L18, it uses the sign of the score to predict +1 or -1. The update around L19–21 runs only when the prediction is wrong. For HAR, perceptron_ovr.py trains six binary Perceptrons and chooses the class with the largest raw score using argmax. In ML-From-Scratch, fit uses a linear score at L47, Sigmoid at L48, and gradient-based learning at L50–56. Although the file is named Perceptron, it is closer to the Delta / one-layer neural network style than my Rosenblatt Perceptron.

## D. One controlled experiment

The question was: How does my OvR Perceptron compare with sklearn Perceptron on the same HAR split with seed 42, learning rate 0.1, and 10 epochs? My OvR model got Macro-F1 0.836 and accuracy 0.823. sklearn got Macro-F1 0.862 and accuracy 0.855. This was one controlled run, so I do not treat the difference as a final conclusion. The majority baseline was about 0.053, and the Decision Tree on the same split was about 0.81. Results: results/perceptron_benchmark.json; script: experiments/part1_pre_midterm/run_perceptron_benchmark.py.

## E. Failure / misconception

The confusion matrix shows many errors between SITTING, STANDING, and LAYING. These classes are harder to separate with simple linear boundaries. I also corrected my earlier idea that a binary Perceptron could directly use all six HAR labels. For this task, I need six binary classifiers and then choose the class with the highest score.

## F. Written-exam capsule

A Perceptron is a simple linear binary classifier. It uses the input features, weights, and bias to predict +1 or -1. When the prediction is wrong, it updates the weights and bias. It works when the data is linearly separable, but it cannot solve XOR because XOR cannot be separated by one straight line. The Delta rule uses the size of the prediction error and gradient-based learning. In simple words, the Perceptron is mistake-driven, while the Delta rule is error-driven.

## G. Reflection

Before this week, I mainly saw the Perceptron as a simple linear classifier. Now I can write the update rule, explain its geometry, build a 6-class OvR version, and distinguish the Rosenblatt rule from the reference implementation. I still need to tune the learning rate and epochs on the validation set. Next is W06: MLP and backpropagation.

## H. Inquiry trail

* Question asked AI: How does the Perceptron update weights, why does XOR fail, and how can a binary Perceptron be used for six-class HAR?
* Pre-AI evidence: commit 9660873, including exercises/w05-first-attempt.pdf and src/from_scratch/perceptron_first_attempt.py.
* Hint received: check the score, sign decision, update rule, the +1/-1 label format, and the need for One-vs-Rest for six classes.
* Verify: Mitchell §4.4, NPTEL Week 4, and assignment §4.
* Reproduce without AI: I can reproduce the Perceptron update and explain the OvR idea from my own code.
