# 7/17/2020 Saidakbar P
# We will train a linear regression on HackerNews data article headlines and see if the title results in higher upvotes.
#To convert headlines into numerical representation, we will use the bag of words model.
import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()
# separate each word
tokenized_headlines = []
for i, row in submissions.iterrows():
    tokenized_headlines.append(row['headline'].split())
	
punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
# remove punctuations and make all lowewrcase
clean_tokenized = []
for item in tokenized_headlines:
    tokens = []
    for token in item:
        token = token.lower()
        for punc in punctuation:
            token = token.replace(punc, "")
        tokens.append(token)
    clean_tokenized.append(tokens)

import numpy as np
unique_tokens = []
single_tokens = []
# create a df only with word that occur more than once
for title in clean_tokenized:
    for word in title:
        if word in single_tokens and word not in unique_tokens:
            unique_tokens.append(word)
        else:
            single_tokens.append(word)
counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)

# count the number of word occurrances in the title
for i, title in enumerate(clean_tokenized):
    for x, word in enumerate(title):
        if word in unique_tokens:
            counts.iloc[i][word]+=1
        
# word count to eliminate words with frequency of f<=5 or f>=100
word_counts = counts.sum(axis=0)
counts = counts.loc[:,(word_counts >= 5) & (word_counts <= 100)]

from sklearn.model_selection import train_test_split
# split data into train test
X_train, X_test, y_train, y_test = train_test_split(counts, submissions["upvotes"], test_size=0.2, random_state=1)

from sklearn.linear_model import LinearRegression
# train linear regression
clf = LinearRegression()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

# calculate mse
mse = np.mean(np.power((y_test - predictions), 2)) # 2651. rmse=51.5. This is way off from Stdev of 39.5 for the target variable.
# Our model rmse needs to be as close to stdev as  possible to make meaningful predictions
