# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello World\n")

#import libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:,:-1].values

y = dataset.iloc[:,-1].values
print(y)