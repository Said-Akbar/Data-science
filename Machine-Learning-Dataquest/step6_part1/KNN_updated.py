# 11/12/2019 created by SaidakbarP
# The process of discovering patterns in existing data to make a prediction is called machine learning
# KNN is a method of predicting a numeric value for a new observation using the similarity metric with Euclidian distance.

import pandas as pd
import numpy as np

dc_listings = pd.read_csv("dc_listing.csv") # read in the dataset

# e.g. if we want to calculate the Euclidian distance between a living space that has 3 people and the first listed house in the data, we use ((a-b)**2)**1/2 = abs(a-b)
first_distance = abs(3-dc_listings['accommodates'][0]) # |3-2|=1
# the closer the distance to 0 the more similar the living spaces are.

# we can calculate the distance between our 3 people house and all other listings for the entire column:
dc_listings['distance'] = dc_listings['accommodates'].apply(lambda x: abs(x-3))

# shows how many listings have accomodation for 3 people (houses with zero distance):
print(dc_listings['distance'].value_counts().loc[0]) # 461 listings with 0 distance

# To avoid biasing the results to the ordering of the dataset, we shuffle the records
np.random.seed(1) # set the random set for reproducability

randomized = np.random.permutation(dc_listings.index) # randomize the indices
dc_listings = dc_listings.loc[randomized]
dc_listings = dc_listings.sort_values("distance") # sort by ascending distance. Because we have 461 zero distance listings, shuffling is the only way to make their order random
												#	if we don't randomize, we 461 zeros do not get sorted because there is no rule additional rule to sort equal values (zeros). 
												#	e.g. distance column before randomization: [0] 0 [1] 0 [2] 0 [3] 0 [4] 0
												#	e.g. distance column after randomization: [4] 0 [2] 0 [0] 0 [3] 0 [1] 0. This makes sure the listings are randomized.
print(dc_listings["price"].head(10))

# To calculate the price of our house, we will need to clean the 'price' column and take the mean of the first five rows.
dc_listings['price'] = dc_listings['price'].str.replace(r',','').str.replace(r'$','').astype(float)
mean_price = dc_listings['price'][:5].mean()
print(mean_price) # 156.6. This is our first prediction

# the function that calculates the distance for any new listing with a given number of people:
def predict_price(new_listing):
    temp_df = dc_listings.copy()
    
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: np.absolute(x-new_listing))
    temp_df = temp_df.sort_values('distance') # newer version of python might sort differently and we might get different results.
    predicted_price = temp_df['price'][:5].mean()
    return predicted_price

acc_one = predict_price(1) # 68
acc_two = predict_price(2) # 112.8
acc_four = predict_price(4) # 124.8
print(acc_one, acc_two, acc_four)

# Evaluation of the model performance. We need to split the dataset into test and training so that we can evaluate how our model is predicting the test set.
# We can use 75% of the dataset as train and 25% as test

train = dc_listings.iloc[:2792].copy()
test_df = dc_listings.iloc[2792:].copy() 
print('test size:', test_df.shape)

def predict_price(new_listing, col):
    temp_df = train.copy()
    
    temp_df['distance'] = temp_df[col].apply(lambda x: abs(x-new_listing))
    temp_df = temp_df.sort_values('distance') # newer version of python might sort differently and we might get different results.
    predicted_price = temp_df['price'][:5].mean()
    return predicted_price
	
# get  predicted price for each observation in the test set
test_df['predicted_price'] = test_df['accommodates'].apply(predict_price, col='accommodates')

# error metric is the number that shows how far off we are from actual outcome values
# We use mean absolute error to take into account both negative and positive distances 
mae = (np.absolute(test_df['predicted_price'] - test_df['price'])).mean() # 56.29
print('MAE:', mae)
# We can use mean squared error to penalize the errors better:
mse = (np.square(test_df['predicted_price'] - test_df['price'])).mean() # 18646.5
print('mse for accomadate model:', mse)

# is mse value of 18646.5 high or low? the only way to know this is to compare with other model's mse. Here we predict using bathrooms and calculate the mse:

test_df['predicted_price'] = test_df['bathrooms'].apply(predict_price, col='bathrooms')
test_df['squared_error'] = np.square(test_df['predicted_price']-test_df['price'])
mse = test_df['squared_error'].mean()	
print('MSE for bathroom model:', mse)
	
# Root mean squared error is an error metric whose units are the base unit (in our case, dollars). RMSE for short, this error metric is calculated by taking the square root of the MSE value
rmse = mse**(1/2)

# To see the effect of how RMSE and MAE change in respond to errors, let us see this example:
errors_one = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10])
errors_two = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 1000])
mae_one = errors_one.mean() # 7.5
rmse_one = np.sqrt((errors_one**2).mean()) # 7.9
mae_two = errors_two.mean() # 62.5
rmse_two = np.sqrt((errors_two**2).mean()) # 235.8

print('rmse_one: {}\nrmse_two: {}'.format(rmse_one,rmse_two))