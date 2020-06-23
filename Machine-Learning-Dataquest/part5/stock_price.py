import pandas as pd
import datetime as dt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
# stock price prediction with linear regression

data = pd.read_csv('sphist.csv')
data['Date']=pd.to_datetime(data['Date'])
data = data[data['Date']<dt.datetime(2015,4,1)]
data = data.sort_values('Date',ascending=True)
#print(data.head())

# moving averages
data['5ma'] = data['Close'].rolling(5).sum()
data['5ma']=data['5ma'].shift(1)

data['30ma'] = data['Close'].rolling(30).sum()
data['30ma']=data['30ma'].shift(1)

data['365ma'] = data['Close'].rolling(365).sum()
data['365ma']=data['365ma'].shift(1)

data['Date'] = data[data['Date']> dt.datetime(1951, 1, 2)]

data['5d_avg_vol'] = data['Volume'].rolling(5).sum()
data['5d_avg_vol']=data['5d_avg_vol'].shift(1)
data['dayofweek'] = data['Date'].dt.weekday

data = data.dropna(axis='rows')
# split data
train = data[data['Date'] < dt.datetime(2013,1,1)]
test = data[data['Date'] >= dt.datetime(2013,1,1)]
#print(train.head())
#print(test.head())

lm = LinearRegression()
features = train.drop(['Close', 'High', 'Low', 'Open', 'Volume', 'Adj Close', 'Date'], 1)
target = train['Close']

lm.fit(features, target)
test_pred = lm.predict(test.drop(['Close', 'High', 'Low', 'Open', 'Volume', 'Adj Close', 'Date'],1))
print(mean_squared_error(test_pred, test['Close']))


