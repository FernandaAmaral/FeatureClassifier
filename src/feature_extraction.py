######################### Feature extraction #############################
#                                                                        #
# Autora: Fernanda Amaral Melo                                           #
# Contato: fernanda.amaral.melo@gmail.com                                #
#                                                                        #
##########################################################################

import matplotlib.pyplot as plt
import numpy as np
import cv2
import csv 
import sys
import os

# Macros
TYPES = ['asphalt', 'danger', 'grass']
PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
THETA = {'0': [0, 1],
        '90': [1, 0],
        '45': [1, 1],
}

class extraction(object):
    def __init__(self,file_name):
        self.rgb = cv2.imread(file_name)
        self.gray = self.rgb2gray()
        self.n_level = 255+1

    def rgb2gray(self):
        gray = np.dot(self.rgb[...,:3], [0.299, 0.587, 0.114]) # Convert to grayscale
        gray = gray.astype(int) # Convert real to integers values

        return gray


    def runner(self):
        self.glcm = self.get_glcm(THETA['0'])
        self.features = self.get_features()

        return self.features


    def get_glcm(self, theta):
        glcm = np.zeros([256,256]).astype(float)
        width = self.gray.shape[0]
        height = self.gray.shape[1]

        for i in range(0, width-1-theta[0]):
            for j in range(0, height-1-theta[1]):
                # grayscale values are the index of glcm
                glcm[self.gray[i,j],self.gray[i + theta[0] , j + theta[1]]] += 1
        glcm = glcm/((width - theta[0]) * (height - theta[1]))

        return glcm

    def get_features(self):
        I, J = np.ogrid[0:self.n_level, 0:self.n_level]
        mean_x , mean_y = [0, 0]
        
        for i in range(0,self.n_level):
            for j in range(0,self.n_level):
                mean_x+=i*self.glcm[i,j]
                mean_y+=j*self.glcm[i,j]

        std_x = np.sqrt((self.glcm*(I-mean_x)**2).sum()) # Standard deviation
        std_y = np.sqrt((self.glcm*(J-mean_y)**2).sum())

        features = []
        features.append (( self.glcm * (I-J)**2 ).sum()) # Contrast
        features.append((( self.glcm * (I*J) - mean_x * mean_y ).sum()) / (std_x * std_y) ) # Correlation
        features.append((self.glcm**2).sum()) # Energy
        features.append((self.glcm/(1+np.abs(I-J))).sum()) # Homogeneity

        return features


images = np.arange(1, 50, 2) # odd images are used for training dataset
for type_ in TYPES:
    with open(PATH + 'csv/training/' + type_ + '.csv', 'a') as f:
        for image in images: 
            if (image<10):
                get_features = extraction(PATH + 'Images/' + type_+ '/' + type_ + '_0' + str(image) + '.png')
            else:
                get_features = extraction(PATH + 'Images/' + type_ + '/' + type_ + '_' + str(image) + '.png')

            writer = csv.writer(f)
            writer.writerow(get_features.runner())

images = np.arange(2, 51, 2) # even images are used for testing dataset
for type_ in TYPES:
    with open(PATH + 'csv/testing/' + type_ + '.csv', 'a') as f:
        for image in images: 
            if (image<10):
                get_features = extraction(PATH + 'Images/' + type_+ '/' + type_ + '_0' + str(image) + '.png')
            else:
                get_features = extraction(PATH + 'Images/' + type_ + '/' + type_ + '_' + str(image) + '.png')

        writer = csv.writer(f)
        writer.writerow(get_features.runner())
