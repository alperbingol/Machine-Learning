# -*- coding: utf-8 -*-
"""AlperBingol-HW4_LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NZsUNbfs5oIMtXQFgVwcWou5SX6v1XF3

# Load the dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt                   

df = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/Evaluate-Improve-Models/master/house_prices.csv')
df.sample(5)

"""# "Garage Area" and "SalesPrice" features are selected to analyze."""

new_df = df[['Garage Area','SalesPrice']]
new_df.head()

"""## Convert the data into numpy arrays of two variables, X and y."""

X = np.array(new_df[['Garage Area']])
y = np.array(new_df[['SalesPrice']])
print(X.shape) # Vewing the shape of X
print(y.shape) # Vewing the shape of y

"""## Split train and test data with 0.2 ratio."""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

"""# Linear Regression
Train a linear regression.
"""

from sklearn import linear_model 

regressor = linear_model.LinearRegression()
regressor.fit(X_train,y_train)

"""## Calculate train and test R2."""

from sklearn.metrics import r2_score

y_pred1 = regressor.predict(X_train)
print("Train:", r2_score(y_train,y_pred1))

y_pred2= regressor.predict(X_test)
print("Test:", r2_score(y_test,y_pred2))

"""## Print the bias and the slope."""

print('Regressor coeffient or slope:',regressor.coef_[0][0])
print('Interception point with axis:',regressor.intercept_[0])

"""## Plot the test set with scatter plot and add the linear regression model line.
Remember linear regression recitation.
"""

# Plot a graph with X_test vs y_test
plt.scatter(X_test,y_test,color="blue")
# Regressior line showing

plt.plot(X_train,y_pred1,color="red",linewidth=3)
plt.title('Regression(Test Set)')
plt.xlabel('Garage Area')
plt.ylabel('Sales Price')
plt.show()

"""# Multiple Linear Regression
Select all features.
"""

df_all = df.drop('SalesPrice',1)


X = df_all
y = df['SalesPrice']
print(X.shape) # Vewing the shape of X
print(y.shape) # Vewing the shape of y

"""## Rescale the input features. Use MinMaxScaler."""

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X=(scaler.fit_transform(X))
print(X)

"""## Train test split."""

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

"""## Fit regression model."""

regressor = linear_model.LinearRegression()
regressor.fit(X_train,y_train)

"""## Calculate train and test R2."""

y_pred1 = regressor.predict(X_train)
print("Train:", r2_score(y_train,y_pred1))

y_pred2= regressor.predict(X_test)
print("Test:", r2_score(y_test,y_pred2))

"""## Print the regression coefficients."""

print('Regressor coeffients for multiple linear regression:',regressor.coef_)

"""# Ridge Regression
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html

https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html

## Use cross-validation to estimate alpha. Set the fold size to 5.
"""

from sklearn.model_selection import KFold
from sklearn.linear_model import RidgeCV
kfold = KFold(n_splits=5)

alphas=[1e-3, 1e-2, 1e-1, 1, 2, 5, 8, 10]
# Create and fit model
model_rcv = RidgeCV(alphas,cv=kfold,normalize =True)
# code comes here
model_rcv.fit(X_train, y_train)

"""## Calculate the train and test R2."""

y_pred3 = model_rcv.predict(X_train)
print("Train:", r2_score(y_train,y_pred3))

y_pred4= model_rcv.predict(X_test)
print("Test:", r2_score(y_test,y_pred4))

"""## Print the best alpha."""

print("Alpha:", model_rcv.alpha_)

"""## Print the regression coefficients."""

print('Regressor coeffients for ridge regression:',model_rcv.coef_)

"""Alper Bingol / 23661"""