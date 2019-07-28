# Quartiles
# Task description: https://www.hackerrank.com/challenges/s10-quartiles/problem
int(input())
X1 = sorted(list(map(int, input().split())))

def medianX(X):
    count = len(X)

    if count % 2 == 0:
        mid = round(count/2)
        median = (X[mid] + X[mid-1])/2
    else:
        mid = round(count/2)
        median = X[mid]
    return round(median), mid

median50, center = medianX(X1)
median25, _ = medianX(X1[:center])
median75, _ = medianX(X1[-center:])

print(median25)
print(median50)
print(median75)
