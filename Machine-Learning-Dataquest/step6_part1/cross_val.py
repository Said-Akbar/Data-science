"""
11/15/2019 created by SaidakbarP
SKLEARN KNN
holdout validation
In holdout validation, we usually use a 50/50 split instead of the 75/25 split from train/test validation. 
This way, we remove the number of observations as a potential source of variation in our model performance.
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

split_one = dc_listings[:1862]
split_two = dc_listings[1862:]
# creating two different test-train sets
train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn = KNeighborsRegressor()
knn.fit(train_one[['accommodates']], train_one['price'])
predict_one = knn.predict(test_one[['accommodates']])
iteration_one_rmse = np.sqrt(mean_squared_error(test_one['price'], predict_one))
# swapped data:
knn.fit(train_two[['accommodates']], train_two['price'])
predict_two = knn.predict(test_two[['accommodates']])
iteration_two_rmse = np.sqrt(mean_squared_error(test_two['price'], predict_two))

avg_rmse = np.mean([iteration_one_rmse,iteration_two_rmse])

# k-fold cross validation
# now we divide our dataset into 5 equal parts
dc_listings.loc[dc_listings.index[0:745], "fold"] = 1
dc_listings.loc[dc_listings.index[745:1490], "fold"] = 2
dc_listings.loc[dc_listings.index[1490:2234], "fold"] = 3
dc_listings.loc[dc_listings.index[2234:2978], "fold"] = 4
dc_listings.loc[dc_listings.index[2978:3723], "fold"] = 5

print(dc_listings['fold'].value_counts())

# let us train on folds 2 to 5
knn = KNeighborsRegressor()
new_set = dc_listings[dc_listings['fold']!=1]

knn.fit(new_set[['accommodates']], new_set['price'])
pred = knn.predict(dc_listings[dc_listings['fold']==1][['accommodates']])

iteration_one_rmse = np.sqrt(mean_squared_error(dc_listings[dc_listings['fold']==1]['price'], pred))
print('fold 1 RMSE:', iteration_one_rmse)

# function to perform cross validation:
fold_ids = [1,2,3,4,5]

def train_and_validate(df, folds):
    rmse_list = []
    for k in folds:
        train = df[df['fold']!=k]
        test = df[df['fold']==k]
        knn = KNeighborsRegressor()
        knn.fit(train.drop(['price', 'fold'], axis=1), train['price'])
        preds=knn.predict(test.drop(['price','fold'], axis=1))
        rmse_list.append(np.sqrt(mean_squared_error(test['price'], preds)))
    return rmse_list

rmses = train_and_validate(dc_listings[['accommodates', 'price', 'fold']], fold_ids)
avg_rmse = np.mean(rmses)
print('5 fold cross validation: ', rmses, avg_rmse)

# cross validation with sklearn
from sklearn.model_selection import cross_val_score, KFold

kf = KFold(5, shuffle=True, random_state=1)
knn = KNeighborsRegressor()
mses = cross_val_score(knn, dc_listings[['accommodates']], dc_listings['price'], cv=kf, scoring="neg_mean_squared_error")
avg_rmse = np.mean(np.sqrt(np.absolute(mses)))
print('sklearn avg_rmse:', avg_rmse)
# k = 10 is standard cross validation number



