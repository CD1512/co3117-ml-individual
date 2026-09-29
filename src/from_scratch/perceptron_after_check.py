import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0.0

    def fit(self, X, y):
        # y must be +1 or -1
        if not np.all(np.isin(y, [-1, 1])):
            raise ValueError("y must contain only +1 and -1.")

        self.weights = np.zeros(X.shape[1])
        self.bias = 0.0

        for _ in range(self.epochs):
            for x_i, y_i in zip(X, y):

                score = np.dot(x_i, self.weights) + self.bias

                y_pred = 1 if score >= 0 else -1

                if y_pred != y_i:
                    self.weights += self.learning_rate * y_i * x_i
                    self.bias += self.learning_rate * y_i

    def decision_function(self, X):
        """Return the raw linear score."""
        return np.dot(X, self.weights) + self.bias
        
    def predict(self, X):
        score = np.dot(X, self.weights) + self.bias
        return np.where(score >= 0, 1, -1)