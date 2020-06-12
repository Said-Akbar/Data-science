import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
# split into test train
train = data[:1460]
test = data[1460:]
cols=[]
# get int and float only
for col in train.columns:
    if train[col].dtype=='int' or train[col].dtype=='float':
        cols.append(col)
# drop useless columns
numerical_train = train[cols].drop(['PID', 'Year Built', 'Year Remod/Add',
                                   'Garage Yr Blt', 'Mo Sold', 'Yr Sold'], axis='columns')
# keep only non-null columns
nulls=numerical_train.isnull().sum()
null_series=pd.Series(nulls)
full_cols_series = null_series[(null_series==0)]
train_subset = train[full_cols_series.index]
# check correlation between selected features and target
sorted_corrs=abs(train_subset.corr()['SalePrice']).sort_values()
import seaborn as sns
import matplotlib.pyplot as plt
# we can keep features that have corr of higher than 0.3 (you can experiment with this)
# we need to address collinearity in our dataset. It is when two features are highly correlated. if vars are highly correlated then we need to keep one as others are duplicates.
strong_corrs=sorted_corrs[sorted_corrs>0.3]
corrmat=train_subset[strong_corrs.index]
sns.heatmap(corrmat.corr())

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
# get useful fields
final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'
clean_test=test[final_corr_cols.index].dropna()
# train the model
lm = LinearRegression()
lm.fit(train[features],train[target])

test_predictions = lm.predict(clean_test[features])
train_predictions = lm.predict(train[features])
# calculate rmse
test_rmse = np.sqrt(mean_squared_error(test_predictions, clean_test[target]))
train_rmse = np.sqrt(mean_squared_error(train_predictions, train[target])) 
# scale features
unit_train = (train[features] - train[features].min())/(train[features].max()-train[features].min())
unit_train.describe()

# let us drop a feature with the lowest variance
clean_test = test[final_corr_cols.index].dropna()
features=features.drop('Open Porch SF')

lr = LinearRegression()
lr.fit(train[features], train[target])

train_predictions = lr.predict(train[features])
test_predictions = lr.predict(clean_test[features])

train_rmse_2 = np.sqrt(mean_squared_error(train_predictions, train[target]))
test_rmse_2 = np.sqrt(mean_squared_error(test_predictions, clean_test[target]))

