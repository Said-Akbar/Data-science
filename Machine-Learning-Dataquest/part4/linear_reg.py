# 11/20/2019 created by SaidakbarP
# Linear regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data[:1460]
test = data[1460:]
data.info()
target = 'SalePrice'

# for simple univariate linear regression, we need to select a feature that has a linear relationship with target 
# let us check some features
import seaborn
fig = plt.figure(figsize=(7,15))

ax1 = fig.add_subplot(3,1,1)
train.plot('Garage Area', 'SalePrice', ax=ax1, kind='scatter')

ax2 = fig.add_subplot(3,1,2)
train.plot('Gr Liv Area', 'SalePrice', ax=ax2, kind='scatter')

ax3 = fig.add_subplot(3,1,3)
train.plot('Overall Cond', 'SalePrice', ax=ax3, kind='scatter')
plt.show()

# GR liv Area is highly correlated. Let us go with it:
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])
a0 = lr.intercept_
a1 = lr.coef_
print('linear model parameters:', a0, a1)

# show accuracy metrics
from sklearn.metrics import mean_squared_error

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])

tr = lr.predict(train[['Gr Liv Area']])
test1 = lr.predict(test[['Gr Liv Area']]) 
                
train_rmse = np.sqrt(mean_squared_error(tr,train['SalePrice']))
test_rmse = np.sqrt(mean_squared_error(test1, test['SalePrice']))
print('univariate reg accuracy metrics:', train_rmse, test_rmse)

# multivariate regression

cols = ['Overall Cond', 'Gr Liv Area']
lr.fit(train[cols], train['SalePrice'])

train_rmse_2 = np.sqrt(mean_squared_error(lr.predict(train[cols]), train['SalePrice']))

test_rmse_2 = np.sqrt(mean_squared_error(lr.predict(test[cols]), test['SalePrice']))                      
print('multivariate reg accuracy metrics:', train_rmse_2, test_rmse_2)
