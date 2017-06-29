# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:09:52 2017

@author: Andrew Laird
"""
# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Taking care of missing data
"""

No need to fix data
"""
#data has no holes now
"""
No need to encode the data

"""
#splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2) #suggested random_state = 0
"""unused
# Feature Scaling 
Feature scaling done by linear regression model
"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
#fits the regressor object to the data
regressor.fit(X_train,y_train)

#predicts what y_test is
y_pred = regressor.predict(X_test)