# source:https://www.python-engineer.com/courses/mlfromscratch/06_perceptron/
import numpy as np


class perceptron:

    def __init__(self, learning_rate=0.01, n_iter=100):
        self.weights = None
        self.bias = None
        self.lr = learning_rate
        self.n_iter = n_iter
        self.activation_func = self._uni_step_func

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0
        y_ = np.array([1 if i == 'joy' else 0 for i in y])
        for i in range(self.n_iter):
            for index, value in enumerate(X):
                linear_output = np.dot(value, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)

                update = self.lr * (y_[index] - y_predicted)

                self.weights += update * value
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    # activation function
    def _uni_step_func(self, x):
        return np.where(x >= 0, 1, 0)