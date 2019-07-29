# Interquartile Range. HackerRank statistics problem.
# link with description: https://www.hackerrank.com/challenges/s10-interquartile-range/problem
int(input())
X = input().split()
freq = input().split()
dataset = ""

for i, val in enumerate(X):
    dataset +=((val+" ")*int(freq[i]))

X1 = sorted(list(map(float, dataset.split())))

def medianX(X):
    count = len(X)
    #print(X)
    if count % 2 == 0:
        mid = (count//2)
        median = (X[mid] + X[mid-1])/2
    else:
        mid = (count//2)
        median = X[mid]
    return round(median,1), mid

median50, center = medianX(X1)
Q1, _ = medianX(X1[:center])
Q3, _ = medianX(X1[-center:])
IQR = Q3-Q1

print(IQR)
