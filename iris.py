# -*- coding: utf-8 -*-
"""Iris

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10A-us6tEtW8Ngtdx8_w8vx17DeStFPAd

IMPORTIMG LIBRARIES
"""

# Commented out IPython magic to ensure Python compatibility.
#IMPORTING ALL THE ESSENTIAL LIBRARIES FOR THE PROJECT

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# %matplotlib inline

"""LOADING THE DATASET"""

df.describe()

columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class_labels']
 # Load the data
 df = pd.read_csv('iris.data', names=columns)
 df.head()

"""VISUALIZATION OF OUR DATASET"""

df.describe()

df = df[~df.index.duplicated()]

# Visualize the whole dataset
sns.pairplot(df, hue='class_labels')

"""SEPARATING INPUT COLUMN AND OUTPUT COLUMN"""

# Separate festures and target
data = df.values

X = data[:,0:4]
Y = data[:,4]

"""SPLITTING THE DATA INTO TRAINING AND TESTING"""

# Split the data to train and test the dataset.
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
print(X_train)

"""SUPPORT VECTOR MACHINE ALGORITHM"""

#Support vector machine algorithm
from sklearn.svm import SVC 

model_svc = SVC()
model_svc.fit(X_train, Y_train)

prediction1 = model_svc.predict(X_test)
#Calculate the accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score,(Y_test, prediction1))

"""MODEL2: LOGISTIC REGRESSION"""

#LOGISTIC REGRESSION
from sklearn.linear_model import LogisticRegression
model_LR=LogisticRegression()
model_LR.fit(X_train,Y_train)

prediction2 = model_LR.predict(X_test)
#Calculate the accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, prediction2))

"""MODEL3: Decision Tree Clasifier"""

#DecisionTreeClasifer
from sklearn.tree import DecisionTreeClassifier
model_DTC = DecisionTreeClassifier()
model_DTC.fit(X_train,Y_train)

prediction3 = model_svc.predict(X_test)
#Calculate the accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, prediction3))

#A detailed classification report
from sklearn.metrics import classification_report
print(classification_report(Y_test, prediction2))

X_new = np.array([[3, 2, 1, 0.2], [4.9, 2.2, 3.8, 1.1], [5.3, 2.2, 4.6, 1.9]])
#Prediction of the species from the input vector
prediction = model_svc.predict(X_new)
print("Prediction of species: {}".format(prediction))