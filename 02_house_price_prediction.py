# This is a HackerRank problem on Predicting House Prices
# https://www.hackerrank.com/challenges/predicting-house-prices/problem
# My solution to the problem successfully passed all test cases.
import pandas as pd
a=input()
nfeat = a.split()[0]
nrows = int(a.split()[1])
ntrain=[]
df = pd.DataFrame([])

for i in range(0, nrows):
   line=input()
   row=line.split()
   ntrain.append(row)
df1 = pd.DataFrame(ntrain) 
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree= int(nfeat))

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
X = df1.iloc[:, :-1]
#print(X)
y=df1.iloc[:,-1]
#print(y)
X_poly = poly.fit_transform(X)
lm.fit(X,y)
#print(lm.coef_)
ntest= input()
testlist=[]
for i in range(0,int(ntest)):
   line=input()
   row=line.split()
   testlist.append(row)
dftest = pd.DataFrame(testlist) 
#print(dftest)
pred=lm.predict((dftest))
for i in range(0, len(pred)):
   print(pred[i])

