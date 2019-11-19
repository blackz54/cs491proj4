import numpy as np
import matplotlib.pyplot as plt


# Function to compute the Z matrix required for PCA
def compute_Z(X, centering=True, scaling=True):
    Z = []
    if centering:
        column_averages = [compute_mean(X[:, i]) for i in range(len(X[0]))]
        Z = np.array([subtract(X[:, i], column_averages[i]) for i in range(len(X[0]))]).transpose()
    if scaling:
        column_std = [compute_std_dev(X[:, i]) for i in range(len(X[0]))]
        Z = np.array([divide(Z[:, i], column_std[i]) for i in range(len(Z[0]))]).transpose()
    return Z


# Function which computes covariance matrix
def compute_covariance_matrix(Z):
    zT = np.array(Z).transpose()
    return np.dot(zT, Z)


# Function to find the principal components of the covariance matrix.
# Assumption here is that covariance matrix will always be square and that col index of eig[0] will
#   be the eigenvalue for the same row index at eig[1]
# return eig[0]: eigenvalues
# return eig[1]: eigenvectors
def find_pcs(COV):
    eig = np.linalg.eig(COV)
    return eig[0], eig[1]


def project_data(Z, PCS, L, k, var):
    pass


# Helper function to calculate the mean of a column of data
def compute_mean(X):
    return np.mean(X)


# Helper function to calculate the standard deviation of a column of data
def compute_std_dev(X):
    return np.std(X)


# Helper function to subtract the average of a column of data from each element in that column
def subtract(X, avg):
    return np.subtract(X, avg)


# Helper function to divide each element in a column of data by that columns standard deviation
def divide(X, std):
    return np.divide(X, std)
