from sklearn.datasets import make_regression # package for generating a random dataset
import pandas as pd

reg_data = make_regression(n_samples=100, n_features=3, random_state=1) # this returns a tuple
features = pd.DataFrame(reg_data[0]) # the first element is features
labels = pd.Series(reg_data[1]) # next element contains labels for each row
# ----------------------
from sklearn.linear_model import SGDRegressor
# this function runs gradient descent on features to fit into labels. Returns weights/coefficients of the linear regression
def train(features, labels):
    lr = SGDRegressor()
    lr.fit(features, labels)
    return lr.coef_
# feedforward takes features of the dataset and coefficients of the linear regression and performs matrix multiplication to get predicted y
def feedforward(features, weights):
    return np.dot(features, weights)
    

features['bias'] = 1 # intercept weight is always 1


# Uncomment after you've implemented train() and feedforward()
train_weights = train(features, labels)
linear_predictions = feedforward(features, train_weights)

from sklearn.datasets import make_classification
# we will generate a dataset for classification now
dataset = make_classification(n_samples=100, n_features=4, random_state=1)
# returns features and labels similar to make_regression
class_features = pd.DataFrame(dataset[0])
class_labels = pd.Series(dataset[1])

#-------
# implemeting logistic regression as an activation function
class_features['bias'] = 1
# gradient descent fitting
def log_train(class_features, class_labels):
    lr = SGDClassifier()
    lr.fit(class_features, class_labels)
    return lr.coef_
# transform output into 0 and 1
def sigmoid(linear_combination):
    return 1/(1+np.exp(-linear_combination))

def log_feedforward(class_features, log_train_weights):
    # perform gradient descent fitting
    linear_combination = np.dot(class_features, log_train_weights.T)
    # perform sigmoid transformation
    log_predictions = sigmoid(linear_combination)
    # perform classification
    log_predictions[log_predictions >= 0.5] = 1
    log_predictions[log_predictions < 0.5] = 0
    return log_predictions
    

log_train_weights = log_train(class_features, class_labels)
log_predictions = log_feedforward(class_features, log_train_weights)

