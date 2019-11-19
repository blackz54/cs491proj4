import numpy as np
import matplotlib.pyplot as plt
import pca

X = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
Z = pca.compute_Z(X)
COV = pca.compute_covariance_matrix(Z)
#L, PCS = pca.find_pcs(COV)
#Z_star = pca.project_data(Z, PCS, L, 1, 0)

