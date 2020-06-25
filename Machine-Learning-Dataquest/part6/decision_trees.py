import pandas

# Set index_col to False 
income = pandas.read_csv("income.csv", index_col=False)
print(income.head(5))

# Convert a single column from text categories to numbers
col = pandas.Categorical(income["workclass"])
income["workclass"] = col.codes
print(income["workclass"].head(5))
cols  = ['education', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country', 'high_income']
for x in cols:
    col = pandas.Categorical(income[x])
    income[x] = col.codes
# Split income into two parts based on the value of the workclass column
private_incomes = income[income['workclass']==4]
public_incomes = income[income['workclass']!=4]

import math
# Passing in 2 as the second parameter to math.log will take a base 2 log
entropy = -(2/5 * math.log(2/5, 2) + 3/5 * math.log(3/5, 2))
print(entropy)
ones = income[income['high_income']==1].shape[0]
zeros = income[income['high_income']==0].shape[0]
rows = income.shape[0]
income_entropy = -(ones/rows*math.log(ones/rows, 2)+ (zeros/rows)*math.log(zeros/rows,2))

import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify that our function matches our answer from earlier
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)
agemedian=income['age'].median()
one_split=income[income['age']<=agemedian]
second_split=income[income['age']>agemedian]
age_information_gain = age_split

entropy = calc_entropy(income['high_income'])
age_information_gain = entropy - (one_split.shape[0]/income.shape[0]*calc_entropy(one_split['high_income'])+second_split.shape[0]/income.shape[0]*calc_entropy(second_split['high_income']))

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a data set, column to split on, and target
    """
    # Calculate the original entropy
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data, based on the median
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits and calculate the subset entropies
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain
    return original_entropy - to_subtract

# Verify that our answer is the same as on the last screen
print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]
information_gains = []
for col in columns:
    information_gain = calc_information_gain(income, col, 'high_income')
    information_gains.append(information_gain)
highest_gain = columns[information_gains.index(max(information_gains))]