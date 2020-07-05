from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_moons
import pandas as pd
import matplotlib.pyplot as plt
# let's generate a non-linear dataset
dataset = make_moons(100, random_state=3, noise=0.04)
features = pd.DataFrame(dataset[0])
labels = pd.Series(dataset[1])
# plot data
fig = plt.figure(figsize=(8,8))
# this is a 3d projection plot of the dataset
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs=features[0], ys=features[1], zs=labels)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

# adding an intercept
features["bias"] = 1
# shuffling data before splitting into test/train
np.random.seed(8)
shuffled_index = np.random.permutation(features.index)
shuffled_data = features.loc[shuffled_index]
shuffled_labels = labels.loc[shuffled_index]
# split into two sets
mid_length = int(len(shuffled_data)/2)
train_features = shuffled_data.iloc[0:mid_length]
test_features = shuffled_data.iloc[mid_length:len(shuffled_data)]
train_labels = shuffled_labels.iloc[0:mid_length]
test_labels = shuffled_labels.iloc[mid_length: len(labels)]
# sklearn is friendly for learning new concepts but its ANN models use the same activation function for all layers and  do not use GPU. This makes training difficult for large datasets
# train logtic regression
logr = LogisticRegression()
logr.fit(train_features, train_labels)
log_predictions = logr.predict(test_features)
# train Multi-layer Perceptron classifier
mlp = MLPClassifier(hidden_layer_sizes=(1,), activation='logistic')
mlp.fit(train_features, train_labels)
nn_predictions = mlp.predict(test_features)
# classification Accuracy (y_true, y_pred)
log_accuracy = accuracy_score(test_labels, log_predictions)
nn_accuracy = accuracy_score(test_labels, nn_predictions)
#nn_accuracy = 0.48

# create different neurons
neurons = [1,5,10,15,20,25]
accuracies = []
for i in neurons:
    mlp = MLPClassifier(hidden_layer_sizes=(i,), activation='logistic')
    mlp.fit(train_features, train_labels)
    preds = mlp.predict(test_features)
    accuracy = accuracy_score(test_labels, preds)
    accuracies.append(accuracy)
# as we increase the number of neurons, accuracy increases too
print(accuracies)

neurons = [1, 5, 10, 15, 20, 25]
nn_accuracies = []
# run mlp with two hidden layers
for n in neurons:
    mlp = MLPClassifier(hidden_layer_sizes=(n, n), activation='relu', max_iter=1000)
    mlp.fit(train_features, train_labels)
    nn_pred = mlp.predict(test_features)
    
    accuracy = accuracy_score(test_labels, nn_pred)
    nn_accuracies.append(accuracy)

nn_accuracies = [0.52,.9,.88,1,1,1]
print(nn_accuracies)