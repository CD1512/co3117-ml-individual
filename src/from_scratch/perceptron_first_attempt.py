import numpy as np

class Perceptron: 
    def __init__(self, learing_rate=0.1, epochs=10):
        self.learing_rate = learing_rate
        self.epochs = epochs
        self.weight = None
        self.bias = None

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        
        for _ in range(self.epochs):
            for x_i, y_i in zip(X, y):
                score = np.dot(x_i, self.weights)+ self.bias

                y_pred = 1 if score >= 0 else -1
                if y_pred != y_i:
                    self.weights += self.learing_rate * y_i * x_i
                    self.bias += self.learing_rate * y_i
    
    def predict(self, X):
        score = np.dot(X, self.weights)+ self.bias
        return np.where(score >= 0, 1, -1)


 