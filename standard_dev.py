# standard deviation of a given array
n = int(input())
data = list(map(float,input().split()))
mean = sum(data)/n
summ = sum([(i-mean)**2 for i in data])
sigma = (summ/n)**(1/2)
print(round(sigma,1))