Following are my notes summary for part 5 
## Logistic regression
- For categorical or discrete target predictions, use classification technique
- Logistic regression is a binary classification technique
- Logistic regression outputs values between 0 and 1 (as probability values)
- We define the threshold for the predictions to belong to 0 or 1 (binary. Usually >=51% probability is the threshold for outcome to be 1).

- Logistic regression is a binary classification model
- Accuracy of a logistic regression calculated with (#correct predictions)/(#observations)
- For outcomes of a binary classification we use two terms: Positive for outcomes with 1. Negative for outcomes with 0. (both are for dataset’s y variable)
- Sensitivity measures true positive rate: (true positive)/(false negative + true positive) (remember: all are actual positives)
- Specificity measures True Negative rate: (true negative)/(false positive + true negative) (remember: all are actual negatives)
## Overfitting
- Overfitting is when the model has a low error rate in training set and higher error rate in test set
- Bias (when a model has few features) and variance (when a model has many features) tradeoff helps us find the optimal number of features in which the model has a good accuracy and generalization
- Kfold cross-validation helps us choose the optimal model which satisfies bias-variance tradeoff
## Clustering
- Clustering is an unsupervised learning technique in which you categorize records based on their similarity
- For 2-3 dimensions (fields), euclidean distance is a good measure for a similarity metric.
- K-means technique is a method for categorizing data into K groups.
- Choosing the right K is crucial (point for K is chosen randomly with sklearn)

