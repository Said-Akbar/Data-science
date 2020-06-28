from sklearn.tree import DecisionTreeClassifier
import numpy
import math
import pandas as pd


income = pd.read_csv('income.csv')
# Convert a single column from text categories to numbers
col = pandas.Categorical(income["workclass"])
income["workclass"] = col.codes
print(income["workclass"].head(5))
cols  = ['education', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country', 'high_income']
for x in cols:
    col = pandas.Categorical(income[x])
    income[x] = col.codes
# A list of columns to train with	
columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

# Instantiate the classifier
# Set random_state to 1 to make sure the results are consistent
clf = DecisionTreeClassifier(random_state=1)
# fit
clf.fit(income[columns], income['high_income'])

# Set a random seed so the shuffle is the same every time
numpy.random.seed(1)
# randomize dataset
income = income.reindex(numpy.random.permutation(income.index))
# split data
train_max_row = math.floor(income.shape[0] * .8)
train = income[:train_max_row]
test = income[train_max_row:]
# AUC score
from sklearn.metrics import roc_auc_score

clf = DecisionTreeClassifier(random_state=1)
clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
error = roc_auc_score(test['high_income'], predictions)

# Decision trees model with min_samples_split=13
clf = DecisionTreeClassifier(random_state=1,  min_samples_split=13)
clf.fit(train[columns],train['high_income'])

train_predictions = clf.predict(train[columns])
test_pred = clf.predict(test[columns])

train_auc = roc_auc_score(train['high_income'], train_predictions)
test_auc = roc_auc_score(test['high_income'], test_pred)

# Decision trees model with min_samples_split=13 and max_depth=7. This improves model accuracy 
clf = DecisionTreeClassifier(random_state=1, max_depth=7, min_samples_split=13)
clf.fit(train[columns], train["high_income"])
predictions = clf.predict(test[columns])
test_auc = roc_auc_score(test["high_income"], predictions)

train_predictions = clf.predict(train[columns])
train_auc = roc_auc_score(train["high_income"], train_predictions)

# if we set max_depth=2 the model will underfit the dataset. Therefore, it is important to optimize tree parameters.