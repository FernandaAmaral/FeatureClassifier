######################## Feature classification ##########################
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

class zone_classification (object):
    def __init__(self, type_):
        self.testing_images = np.array(self.read_csv('testing'))
        self.training_images = np.array(self.read_csv('training'))
        self.type_ = type_


    def read_csv(self, dataset):
        images = []
        with open(PATH + 'csv/' + dataset + '/' + type_ + '.csv') as csvfile: # Read csv file 
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
            for row in reader: # each row is a list
                row.pop(1)
                images.append(row)

        return images


    # def runner(self):
    #     print(self.type_)
    #     for testing in self.testing_images:
    #         for training in self.training_images:

    #            accuracy_score(np.array(training),np.array(testing))

    #     return

for type_ in TYPES:
    classificate = zone_classification(type_)
    # classificate.runner()

