# This part of DQ course walks through feature engineering techniques using Titanic dataset
# Saidakbarp 7/12/2020
import pandas as pd
# feature engineering
train = pd.read_csv('train.csv')
holdout = pd.read_csv('test.csv')

def process_age(df):
    df["Age"] = df["Age"].fillna(-0.5)
    cut_points = [-1,0,5,12,18,35,60,100]
    label_names = ["Missing","Infant","Child","Teenager","Young Adult","Adult","Senior"]
    df["Age_categories"] = pd.cut(df["Age"],cut_points,labels=label_names)
    return df

def create_dummies(df,column_name):
    dummies = pd.get_dummies(df[column_name],prefix=column_name)
    df = pd.concat([df,dummies],axis=1)
    return df
# categorize age
train = process_age(train)
holdout = process_age(holdout)

cols = ['Age_categories', 'Pclass', 'Sex']
# get dummies
for col in cols:
    train = create_dummies(train, col)
    holdout = create_dummies(holdout, col)

print(train.columns)

from sklearn.preprocessing import minmax_scale
# The holdout set has a missing value in the Fare column which
# we'll fill with the mean.
holdout["Fare"] = holdout["Fare"].fillna(train["Fare"].mean())
train['Embarked'] = train['Embarked'].fillna('S')
holdout['Embarked'] = holdout['Embarked'].fillna('S')
# get dummies
train = create_dummies(train, 'Embarked')
holdout = create_dummies(holdout, 'Embarked')
# get scaled versions
columns = ['SibSp', 'Parch',  'Fare']
for col in columns:   
    train[col+'_scaled'] = minmax_scale(train[col])
    holdout[col+'_scaled'] = minmax_scale(holdout[col])
	
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
# columns to train on
columns = ['Age_categories_Missing', 'Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior', 'Pclass_1', 'Pclass_2', 'Pclass_3',
       'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
       'SibSp_scaled', 'Parch_scaled', 'Fare_scaled']

lr = LogisticRegression()
# train the model 
lr.fit(train[columns], train['Survived'])
# get lr coefficients
coefficients = lr.coef_
feature_importance = pd.Series(coefficients[0], index = columns)
# plot feature_importance
feature_importance.plot.barh()

from sklearn.model_selection import cross_val_score
import numpy as np
columns = ['Age_categories_Infant', 'SibSp_scaled', 'Sex_female', 'Sex_male',
       'Pclass_1', 'Pclass_3', 'Age_categories_Senior', 'Parch_scaled']

lr = LogisticRegression()
scores = cross_val_score(lr, train[columns], train['Survived'], cv=10)
accuracy=np.mean(scores)

columns = ['Age_categories_Infant', 'SibSp_scaled', 'Sex_female', 'Sex_male',
       'Pclass_1', 'Pclass_3', 'Age_categories_Senior', 'Parch_scaled']

all_X = train[columns]
all_y = train['Survived']
# train on all data
lr = LogisticRegression()
lr.fit(all_X, all_y)
# predict holdouts
holdout_predictions=lr.predict(holdout[columns])
# submit to kaggle
submission = pd.DataFrame({'PassengerId': holdout['PassengerId'], 'Survived': holdout_predictions})
submission.to_csv('submission_1.csv', index=False)

def process_age(df,cut_points,label_names):
    df["Age"] = df["Age"].fillna(-0.5)
    df["Age_categories"] = pd.cut(df["Age"],cut_points,labels=label_names)
    return df

def process_fare(df, cut_points, label_names):
    df['Fare_categories'] = pd.cut(df['Fare'], cut_points, labels=label_names)
    return df
# binning for continuous values
points = [0,12,50,100,1000]
label_names = ['0-12', '12-50', '50-100', '100+']
# create bins
train = process_fare(train, points, label_names)
holdout = process_fare(holdout, points, label_names)
# create dummy columns for each bin
train = create_dummies(train, 'Fare_categories')
holdout = create_dummies(holdout, 'Fare_categories')

titles = {
    "Mr" :         "Mr",
    "Mme":         "Mrs",
    "Ms":          "Mrs",
    "Mrs" :        "Mrs",
    "Master" :     "Master",
    "Mlle":        "Miss",
    "Miss" :       "Miss",
    "Capt":        "Officer",
    "Col":         "Officer",
    "Major":       "Officer",
    "Dr":          "Officer",
    "Rev":         "Officer",
    "Jonkheer":    "Royalty",
    "Don":         "Royalty",
    "Sir" :        "Royalty",
    "Countess":    "Royalty",
    "Dona":        "Royalty",
    "Lady" :       "Royalty"
}
# extract features from text data
# title as a category
extracted_titles = train["Name"].str.extract(' ([A-Za-z]+)\.',expand=False)
train["Title"] = extracted_titles.map(titles)

extracted_titles = holdout['Name'].str.extract('([A-Za-z]+)\.', expand=False)
holdout['Title'] = extracted_titles.map(titles)
# Cabin type as a category
train['Cabin_type'] = train['Cabin'].str[0]
holdout['Cabin_type'] = holdout['Cabin'].str[0]
train['Cabin_type'] = train['Cabin_type'].fillna('Unknown')
holdout['Cabin_type'] = holdout['Cabin_type'].fillna('Unknown')

cols = ['Title', 'Cabin_type']

for col in cols:
    train = create_dummies(train, col)
    holdout = create_dummies(holdout, col)

import numpy as np
import seaborn as sns

def plot_correlation_heatmap(df):
    corr = df.corr()
    
    sns.set(style="white")
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)


    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()

columns = ['Age_categories_Missing', 'Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior', 'Pclass_1', 'Pclass_2', 'Pclass_3',
       'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
       'SibSp_scaled', 'Parch_scaled', 'Fare_categories_0-12',
       'Fare_categories_12-50','Fare_categories_50-100', 'Fare_categories_100+',
       'Title_Master', 'Title_Miss', 'Title_Mr','Title_Mrs', 'Title_Officer',
       'Title_Royalty', 'Cabin_type_A','Cabin_type_B', 'Cabin_type_C', 'Cabin_type_D',
       'Cabin_type_E','Cabin_type_F', 'Cabin_type_G', 'Cabin_type_T', 'Cabin_type_Unknown']

plot_correlation_heatmap(train[columns])

from sklearn.feature_selection import RFECV

columns = ['Age_categories_Missing', 'Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Young Adult',
       'Age_categories_Adult', 'Age_categories_Senior', 'Pclass_1', 'Pclass_3',
       'Embarked_C', 'Embarked_Q', 'Embarked_S', 'SibSp_scaled',
       'Parch_scaled', 'Fare_categories_0-12', 'Fare_categories_50-100',
       'Fare_categories_100+', 'Title_Miss', 'Title_Mr', 'Title_Mrs',
       'Title_Officer', 'Title_Royalty', 'Cabin_type_B', 'Cabin_type_C',
       'Cabin_type_D', 'Cabin_type_E', 'Cabin_type_F', 'Cabin_type_G',
       'Cabin_type_T', 'Cabin_type_Unknown']


# feature elimination with sklearn RFECV function
all_X = train[columns]
all_y = train["Survived"]
lr = LogisticRegression()
selector = RFECV(lr,cv=10)
selector.fit(all_X,all_y)

optimized_columns = all_X.columns[selector.support_]

all_X = train[optimized_columns]
all_y = train["Survived"]
lr = LogisticRegression()
scores = cross_val_score(lr, all_X, all_y, cv=10)
accuracy = np.mean(scores)

lr = LogisticRegression()
lr.fit(all_X, all_y)
holdout_predictions=lr.predict(holdout[all_X.columns])
# our overall accuracy for holdout increased by 2.4% which makes a huge difference in Kaggle leaderboard
submission = pd.DataFrame({'PassengerId': holdout['PassengerId'], 'Survived': holdout_predictions})

submission.to_csv('submission_2.csv', index=False)