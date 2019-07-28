# Calculate the weighted mean
# problem description: https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# numpy is not allowed. No library is allowed

count = int(input())
elements = list(map(float, input().split()))
weights = list(map(float, input().split()))

##########################################
X = []

[X.append(elements[n]*weights[n]) for n, i in enumerate(elements)]

weighted_avg = round(sum(X)/sum(weights), 1)

print(weighted_avg)

#####################################
# or one-liner after reading the data:
# print(round(sum([i[0]*i[1] for i in zip(elements, weights)])/sum(weights),1))
