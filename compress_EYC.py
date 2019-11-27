##########  PROJECT 4 COMPRESS - EYC

import numpy as np
import matplotlib.pyplot as plt
import os


def compress_images(DATA,k):   
    DATA = DATA.T
    ## Center data
    mean_mat = np.mean(DATA,axis=0)
    Z = DATA - mean_mat
    
    ## Compute covariance matrix
    Ztp = Z.T
    COV = np.dot(Ztp,Z)
    
    ## Calculate eigenvalues L and eigenvectors PCS
    L, PCS = np.linalg.eig(COV)
    
    idx = L.argsort()[::-1]
    L = L[idx].real
    PCS = PCS[:,idx].real

    ## Project data onto k eigenvectors
    eucld = np.linalg.norm(PCS, axis=0)
    PCS_norm = PCS/eucld
    
    PCS_new = PCS_norm[:,:k]

    feat_vec = PCS_new.T
    
    Z_star = np.dot(feat_vec,Ztp)    
    
    ## Return data to original mean
    arr = np.dot(feat_vec.T,Z_star)
        
    Output = arr.T + mean_mat
    out_min = np.amin(Output)
    out_max = np.amax(Output)
    Output_norm = (Output - out_min)/(out_max-out_min)  # normalize values between 0-1
    Output_scale = Output_norm * 255  # set to Image values between 0 and 255
    Output_scale = Output_scale.astype(np.uint8)  # return to uint8 data type
    
    ## Check if Output directory exists
    path = 'Data/Output/'
    if not os.path.exists(path):
        os.mkdir(path)
        print ("Directory", path, " created")
    else:
        print("Directory", path, " already exists")

    ## For each row in scaled Output, reshape into original image size and save in correct directory
    for j in range(Output_scale.shape[0]):
        curr_image = Output_scale[j,:]
        reshape_image = curr_image.reshape(image_shape)
        output_path = os.path.join(path,'Out'+filenames[j]+'_k_'+str(k)+'.png')
        plt.imsave(output_path,reshape_image,cmap=plt.get_cmap(name = 'gray'),format='png')
    
    return(Output)




def load_data(input_dir):
    folder = os.fsencode(input_dir)
    global filenames
    filenames =[]
    
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        filenames.append(filename)

    ## Test to see dimensions of DATA array
    temp = plt.imread(str(input_dir + filenames[0]))
    global image_shape  # sets image_shape as global variable
    image_shape = temp.shape
    
    temp_flat = np.ndarray.flatten(temp)
    
    cols = len(filenames)
    rows = len(temp_flat)
    
    DATA = np.zeros((rows,cols),dtype=np.uint8)  # initiate DATA array with zeros of correct size (rows = pixels, cols = images)
    
    for i in range(len(filenames)):
        temp = plt.imread(str(input_dir + filenames[i]))
        temp_flat = np.ndarray.flatten(temp)
        DATA[:,i] = temp_flat
    
    return(DATA)
