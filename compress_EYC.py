##########  PROJECT 4 COMPRESS - EYC

import numpy as np
import matplotlib.pyplot as plt
import os


def compress_images(DATA,k):
    
    
    
    
    
    
    ## Check if Output directory exists
    path = '/Output'
    if (os.path.exists(path) == False):
        os.mkdir(path)
        print ("Created directory %s " % path)
       
    
    
    return(Output)




def load_data(input_dir):
    path = input_dir
    folder = os.fsencode(path)
    filenames =[]
    
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith(('.pgm')):
            filenames.append(filename)
    
    ## Test to see dimensions of DATA array
    temp = plt.imread(str(path + filenames[0]))
    temp_flat = np.ndarray.flatten(temp)
    
    cols = len(filenames)
    rows = len(temp_flat)
    
    DATA = np.zeros((rows,cols))  # initiate DATA array with zeros of correct size (rows = pixels, cols = images)
    
    for i in range(len(filenames)):
        temp = plt.imread(str(path + filenames[i]))
        temp_flat = np.ndarray.flatten(temp)
        DATA[:,i] = temp_flat
    
    return(DATA)



