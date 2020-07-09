# project on Lending Club loan classification data
import pandas as pd

def prediction_fn(predictions):
	tp = len(predictions[(predictions==1)&(loans['loan_status']==1)])
	fp = len(predictions[(predictions==1)&(loans['loan_status']==0)])
	tn = len(predictions[(predictions==0)&(loans['loan_status']==0)])
	fn = len(predictions[(predictions==0)&(loans['loan_status']==1)])

	tpr = tp/(tp+fn)
	fpr = fp/(fp+tn)
	return tpr, fpr

loans = pd.read_csv('cleaned_loans_2007.csv')
loans.info()

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))
# get positive/negatives
fp = len(predictions[(predictions==1) & (loans['loan_status']==0)])
tp = len(predictions[(predictions==1) & (loans['loan_status']==1)])
tn = len(predictions[(predictions==0) & (loans['loan_status']==0)])
fn = len(predictions[(predictions==0) & (loans['loan_status']==1)])
# low fall-out: false positives
fpr = fp/(fp+tn)
# high recall: true positives
tpr = tp/(tp+fn)

from sklearn.linear_model import LogisticRegression
# train a logistic regression
lr = LogisticRegression()
features = loans.drop('loan_status', axis=1)
target = loans['loan_status']

lr.fit(features, target)

predictions=lr.predict(features)

from sklearn.model_selection import cross_val_predict
# do 3-fold cross-validation for the model 
predictions=cross_val_predict(lr, features, target, cv=3)
predictions = pd.Series(predictions)

print(prediction_fn(predictions))

# use class_weight to penalize misclassification of overrepresented class
lr = LogisticRegression(class_weight='balanced')
predictions = cross_val_predict(lr, features, target, cv=3)
predictions = pd.Series(predictions)

print(prediction_fn(predictions))

# specify the penalty for misclassification of smaller class
penalty = {0: 10, 1: 1}
lr = LogisticRegression(class_weight=penalty)
predictions = cross_val_predict(lr, features, target, cv=3)
predictions = pd.Series(predictions)

print(prediction_fn(predictions)) # fpr=9%, tpr=24%. We decreased false positive rate but true positive rate is also low. We want higher tpr to invest into customers who pay off on time

from sklearn.ensemble import RandomForestClassifier
# let us use RandomForestClassifier now
rf = RandomForestClassifier(random_state=1, class_weight='balanced')
predictions = cross_val_predict(rf, features, target, cv=3)
predictions = pd.Series(predictions)

print(prediction_fn(predictions))
# fpr=93%, not a good result. We want to decrease false positives because this helps us avoid customers who default 