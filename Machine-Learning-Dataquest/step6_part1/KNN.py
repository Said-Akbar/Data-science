# 11/12/2019 created by SaidakbarP
# The process of discovering patterns in existing data to make a prediction is called machine learning
# KNN is a method of predicting a numeric value for a new observation using the similarity metric with Euclidian distance.

import pandas as pd
import numpy as np

dc_listing = pd.read_csv("dc_listing.csv") # read in the dataset

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
    
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: abs(x-new_listing))
    temp_df = temp_df.sort_values('distance')
    predicted_price = temp_df['price'][:5].mean()
    return predicted_price

acc_one = predict_price(1) # 68
acc_two = predict_price(2) # 112.8
acc_four = predict_price(4) # 124.8
