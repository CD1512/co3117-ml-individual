# CO3117 — PRE-RELEASE Catch-up (W01–W04)

Author: Tran Chi Dai
Date (actual): 26 / 09 / 2026

## A. Concept capsule

Supervised learning means training a model with data that already has the correct labels. The train set is used to learn from the data, the validation set is used to choose model settings and check overfitting, and the test set is kept untouched for the final evaluation. A Decision Tree works by splitting the data into smaller groups step by step. Impurity tells us how mixed the labels are inside one node. Information gain tells us how useful a split is by measuring how much cleaner the child nodes become after the split. High bias usually happens when the model is too simple and cannot learn the important patterns. High variance happens when the model fits the training data too closely and does not generalize well to new data. We should also keep the test set untouched during preprocessing and model selection so that the final evaluation remains fair.

## B. One worked example

In my release baseline diagnostic (exercises/release-baseline-w01-w04.pdf), I used four samples with two Sunny days labeled No and two Rainy days labeled Yes.

Before splitting, the parent node contains both Yes and No labels, so it is mixed. When I split the data using Weather, the Sunny branch contains only No samples and the Rainy branch contains only Yes samples. Both child nodes are therefore completely pure.

This is a very good split because the two classes are separated perfectly. The impurity after the split becomes zero, so the split gives the maximum possible impurity reduction for this small example. This helped me understand that information gain represents how much cleaner the data becomes after a split.

## C. Code-to-theory trace

The first connection is Gini impurity → impurity_split_first_attempt.py, gini(). The function counts the labels and measures how mixed they are.

The second connection is information gain → best_split(). The code compares the parent impurity with the weighted impurity of the left and right child nodes and keeps the split with the largest gain.

The third connection is midpoint threshold → best_split(). My code creates thresholds between adjacent unique values. This is different from the ML-From-Scratch reference, where candidate threshold values are handled inside its _build_tree() process.

The fourth connection is stopping → impurity_split_after_reference.py, min_samples / min_gain. These conditions prevent the tree from continuing to make very small or weak splits.

After comparing my implementation with the reference, I understood the split process more clearly. The first attempt already had the main impurity and gain ideas, while the reference helped me see how stopping rules fit into a complete tree.

## D. One controlled experiment

I wanted to see what happens when I control the size of the Decision Tree. Using the same HAR split with seed 42, I compared an unconstrained tree, a tree with max_depth=6, and a tree with post-pruning using ccp_alpha.

The unconstrained tree reached a Macro-F1 of 0.8003, with 143 leaves and depth 18. The pre-pruned tree reached 0.8096 Macro-F1, with 23 leaves and depth 6. The post-pruned tree reached 0.8056 Macro-F1, with 26 leaves and depth 9.

Both pruning approaches made the tree much smaller while keeping or slightly improving Macro-F1 on this split. This showed me that controlling tree complexity can help the model generalize better instead of simply making the tree as large as possible.

Source: results/dt_stop_vs_prune.json.

## E. Failure / misconception

One misconception I had was that a very low majority-baseline Macro-F1 automatically means that the pipeline is broken. The majority baseline in results/metrics.csv is about 0.053. Since the HAR task has six classes, a majority classifier predicts only one class, so the other five classes get almost zero F1. Therefore, a Macro-F1 around 0.05 is expected for this simple baseline and does not by itself mean that the pipeline is broken. It is mainly useful as a basic point of comparison.

## F. Written-exam capsule

Impurity measures how mixed the class labels are inside a node. A pure node contains only one class, while a mixed node has higher impurity. Information gain shows how useful a split is by measuring how much the split reduces impurity. A good split creates cleaner child nodes. Pre-pruning stops the tree earlier during training, while post-pruning removes weak branches after the tree has grown. Both methods are used to control model complexity and reduce overfitting.

## G. Reflection

Before this work, I knew that Decision Trees choose the best split, but I did not clearly understand how impurity and information gain were connected to this process. Now I can write the Gini function, calculate the gain for a simple split, and explain how a threshold is selected. I am still not fully confident about how C4.5 handles missing values during splitting and how the alpha value is selected in cost-complexity pruning. Next week, I plan to test my first Perceptron implementation using the same from-scratch approach.

## H. Inquiry trail

The main question I asked was how impurity, information gain, stopping, and pruning are connected to my Decision Tree code, and how I could verify my implementation with a reference implementation.

My pre-AI first attempt was commit 53a67d5. After that, AI helped me read the ML-From-Scratch reference, understand stopping ideas such as min_samples and min_gain, and run the sklearn experiment comparing an unconstrained tree, pre-pruning, and post-pruning.

I verified the ideas by checking decision_tree.py, especially _build_tree() and _calculate_information_gain(), and by recording the mapping in MODEL_LOG.md (Decision Tree section) and in section C above.

After this process, I can now do several parts without AI: write the Gini function, calculate the gain for a simple split, explain midpoint threshold selection, and explain the difference between stopping and pruning.
