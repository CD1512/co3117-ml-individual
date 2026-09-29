import numpy as np

from src.from_scratch.perceptron_after_check import Perceptron


class OneVsRestPerceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.classes = np.arange(1, 7)
        self.classifiers = []

    def fit(self, X, y):
        self.classifiers = []

        for c in self.classes:
            print(f"Training class {c}/6...")

            y_bin = np.where(y == c, 1, -1)

            clf = Perceptron(
                learning_rate=self.learning_rate,
                epochs=self.epochs
            )

            clf.fit(X, y_bin)
            self.classifiers.append(clf)

        return self

    def predict(self, X):
        scores = np.column_stack([
            clf.decision_function(X)
            for clf in self.classifiers
        ])

        best_class = np.argmax(scores, axis=1)

        return self.classes[best_class]