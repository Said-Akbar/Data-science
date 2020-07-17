# 7/13/2020 Saidakbarp - Model Selection
import pandas as pd
train = pd.read_csv('train_modified.csv')
holdout = pd.read_csv('holdout_modified.csv')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np
# let's train our dataset on different models to select the best model
all_X = train.drop(['Survived','PassengerId'],axis=1)
all_y = train['Survived']

lr =LogisticRegression()
scores = cross_val_score(lr, all_X, all_y, cv=10)
accuracy_lr = np.mean(scores)

from sklearn.neighbors import KNeighborsClassifier
# train KNN for predictions
knn = KNeighborsClassifier(n_neighbors=1)
scores = cross_val_score(knn, all_X, all_y, cv=10)
accuracy_knn = np.mean(scores)

import matplotlib.pyplot as plt

def plot_dict(dictionary):
    pd.Series(dictionary).plot.bar(figsize=(9,6),
                                   ylim=(0.78,0.83),rot=0)
    plt.show()

knn_scores = dict()
# let's tune knn parameters
for k in range(1,51,2):
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, all_X, all_y, cv=10)
    knn_scores[k] = np.mean(scores)
    
plot_dict(knn_scores) # 82.4%

from sklearn.model_selection import GridSearchCV
# perform grid search
hyperparameters = {
    "n_neighbors": range(1,20,2),
    "weights": ["distance", "uniform"],
    "algorithm": ['brute'],
    "p": [1,2]
}
knn = KNeighborsClassifier()
grid = GridSearchCV(knn,param_grid=hyperparameters,cv=10)

grid.fit(all_X, all_y)

best_params = grid.best_params_
best_score = grid.best_score_ # 82.7%

from sklearn.ensemble import RandomForestClassifier
import numpy as np
# train random forest
rfs = RandomForestClassifier(random_state=1)
scores = cross_val_score(rfs, all_X, all_y, cv=10)
accuracy_rf = np.mean(scores)

parameters = {
'criterion': ['entropy', 'gini'],
'max_depth': [5, 10],
'max_features': ["log2", "sqrt"],
'min_samples_leaf': [1, 5],
'min_samples_split': [3, 5],
'n_estimators': [6, 9]
}
# hyperparameter tuning for random forests
rfs = RandomForestClassifier(random_state=1)
grid = GridSearchCV(rfs, param_grid=parameters, cv=10)
grid.fit(all_X, all_y)
best_params = grid.best_params_
best_score = grid.best_score_

best_rf = grid.best_estimator_ # 84.3% accuracy with cv
holdout_predictions=best_rf.predict(holdout_no_id)
submission = pd.DataFrame({'PassengerId': holdout['PassengerId'], 'Survived': holdout_predictions})
submission.to_csv('submission_2.csv', index=False)




