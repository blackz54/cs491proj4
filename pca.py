import numpy as np
import matplotlib.pyplot as plt


def compute_Z(X, centering=True, scaling=True):
    Z = []
    if centering:
        column_averages = [compute_mean(X[:, i]) for i in range(len(X[0]))]
        Z = np.array([subtract(X[:, i], column_averages[i]) for i in range(len(X[0]))]).transpose()
    if scaling:
        column_std = [compute_std_dev(X[:, i]) for i in range(len(X[0]))]
        Z = np.array([divide(Z[:, i], column_std[i]) for i in range(len(Z[0]))]).transpose()
    return Z

def compute_covariance_matrix(Z):
    pass


def find_pcs(COV):
    pass


def project_data(Z, PCS, L, k, var):
    pass


def compute_mean(X):
    return np.mean(X)


def compute_std_dev(X):
    return np.std(X)


def subtract(X, avg):
    return np.subtract(X, avg)


def divide(X, std):
    return np.divide(X, std)
