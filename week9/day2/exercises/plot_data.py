import numpy as np
import matplotlib.pyplot as plt


def plot_data(X, y):
    """
    Plots the data points X and y into a new figure.

    Parameters
    ----------
    X : ndarray, shape (n_samples, n_features)
        Training vectors, where n_samples is the number of samples and n_features is the number of features.
    y : ndarray, shape (n_samples,)
        Target values (class labels in classification).
    """
    pos = np.nonzero(y == 1)
    neg = np.nonzero(y == 0)
    plt.plot(X[pos], linestyle='', marker='+', color='k')
    plt.plot(X[neg], linestyle='', marker='o', color='y')
