#### PROJECT 4 PCA - EYC

import numpy as np
import matplotlib.pyplot as plt

#X = np.array([[-1,-1],[-1,1],[1,-1],[1,1]])

## Take data matrix X and standardize given centering and scaling
def compute_Z(X, centering=True, scaling=False):

    if centering == True:
        mean_mat = np.mean(X,axis=0)
        Z = X - mean_mat
        
    if scaling == True:
        stdev = np.std(X,axis=0)
        Z = np.divide(Z,stdev)
    
    return(Z)


## Take standardized matrix Z and return covariance matrix Z.T*Z
def compute_covariance_matrix(Z):
    Ztp = Z.T
    
    COV = np.dot(Ztp,Z)
    
    return(COV)


## Take covariance matrix and return ordered PCS and corresponding L
def find_pcs(COV):
    L, PCS = np.linalg.eig(COV)
    
    idx = L.argsort()[::-1]
    L = L[idx]
    PCS = PCS[:,idx]
    
    return(L, PCS)



## Take inputted data and return projected data, Z_star given k and var
def project_data(Z, PCS, L, k, var):
    eucld = np.linalg.norm(PCS, axis=0)
    PCS_norm = PCS/eucld
    
    if k==0:
        cuml = 0
        for i in range(len(L)):
            cuml += L[i]
            k += 1
            if (cuml/sum(L) >= var):
                PCS_new = PCS_norm[:,:k]
    
    if var==0:
        PCS_new = PCS_norm[:,:k]
        
    feat_vec = PCS_new.T
    Z_adj = Z.T
    
    Z_star = np.dot(feat_vec, Z_adj)    
    
    return(Z_star)