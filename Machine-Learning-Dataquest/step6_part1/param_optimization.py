"""
11/14/2019 created by SaidakbarP
SKLEARN KNN
Simple GRID SEARCH 
Values that affect the behavior and performance of a model that are unrelated to the data that's used are referred to as hyperparameters.
The process of finding the optimal hyperparameter value is known as hyperparameter optimization. 
A simple but common hyperparameter optimization technique is known as grid search. 
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

np.random.seed(1) # set the random set for reproducability

dc_listings = pd.read_csv("dc_listing.csv") # read in the dataset
randomized = np.random.permutation(dc_listings.index) # randomize the indices
dc_listings = dc_listings.loc[randomized]
dc_listings['price'] = dc_listings['price'].str.replace(r',','').str.replace(r'$','').astype(float) # clean price


cols_p = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews', 'price'] 
dc_listings = dc_listings[cols_p]

dc_listings = dc_listings.dropna(axis=0)
print(dc_listings.isnull().sum())

# split data into train test sets

train_df = dc_listings.iloc[:2792]
test_df = dc_listings.iloc[2792:]

# range of K values: 1,2,3,4,5
params = range(1, 6)

cols = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews'] # training cols

def grid_search(hyper_params):
	mse_values = []
	for value in hyper_params: # change K value in each iteration and save new model's mse value 
		knn = KNeighborsRegressor(n_neighbors=value, algorithm='brute')
		knn.fit(train_df[cols], train_df['price'])
		predictions = knn.predict(test_df[cols])
		mse_values.append(mean_squared_error(test_df['price'], predictions))
	return mse_values
	
print('range of K = 1...5: \n', grid_search(params))

# we can widen the range of grid search for parameters:
mse_values=grid_search(range(1,21))
print("\n\n\nrange of K= 1...20: \n", mse_values)	

# There is always some threshold, after which increasing the K does not result in a better accuracy.
# As you increase k at first, the error rate decreases until a certain point, but then rebounds and increases again. 
import matplotlib.pyplot as plt

plt.scatter(range(1,21), mse_values)
plt.title('K value vs MSE')
plt.show()
