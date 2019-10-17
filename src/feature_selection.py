########################## Feature selection #############################
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
FEATURE = ['Contrast', 'Correlation', 'Energy', 'Homogeneity']

class selection(object):
    def __init__(self, type_):
        self.type_ = type_
        self.images = np.array(self.read_csv('training'))
        self.images = np.array(self.images) 
        self.delta =  np.shape(self.images)[1]  # Number of features
        self.selected_features = np.arange(0, self.delta)  # selected_features features index

    def read_csv(self, dataset):
        images = []
        with open(PATH + 'csv/' + dataset + '/' + type_ + '.csv') as csvfile: # Read csv file 
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
            for row in reader: # each row is a list
                images.append(row) 

        return images


    def runner(self):
        self.corr = self.correlation() 
        self.select_feature()
        self.plot()

        return 


    def correlation(self):
        corr = np.zeros([self.delta, self.delta]).astype(float)
        for i in range (0,self.delta):
            for j in range (0,self.delta):
                if i==j: # Avoid repeated pairs 
                    break
                else: # Calculate correlation
                    corr[i,j] = np.correlate(self.images[:,i], self.images[:,j])

        return corr


    def select_feature (self):
        avrg_corr = np.zeros(self.delta).astype(float)
        for feature in self.selected_features: # Average correlation is the mean of all values of a feature
            avrg_corr[feature] = (np.sum(np.abs(self.corr[feature,:])) + np.sum(np.abs(self.corr[:,feature])))/self.delta

        index = int(np.where(avrg_corr == np.max(avrg_corr))[0]) # Find the biggest average correlation
        self.selected_features = np.delete(self.selected_features,[index]) # Delete feature

        return 

    
    def plot(self):
        fig = plt.figure()
        fig.suptitle( 'Selected pairs for ' + str(self.type_))
        subplot_=130
        for feature_x in self.selected_features:
            for feature_y in self.selected_features:
                if feature_x == feature_y:
                    break
                else:
                    subplot_+=1
                    plt.subplot(subplot_)
                    plt.title(str(FEATURE[feature_x]) + ' x ' + str(FEATURE[feature_y]))
                    plt.plot(self.images[:,feature_x], self.images[:,feature_y], 'bo')
        plt.show()
        
        return


for type_ in TYPES:
    select_feature = selection(type_)
    select_feature.runner()

