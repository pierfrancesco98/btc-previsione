from pandas import read_csv
from sklearn import linear_model
from sklearn.metrics import r2_score
import pickle


prezzi = read_csv('BTC-EUR.csv')
X = prezzi[['High','Low']]
Y = prezzi['Close']

modello = linear_model.LinearRegression()
modello.fit(X.values, Y.values)
prev = modello.predict(X.values)
r2 = r2_score(Y.values, prev)


High = 1000
Low = 500
previsione =  modello.predict([[High,Low]])

modello_r2_tuple = (modello, r2)

with open('modello.pkl', 'wb') as file:
    pickle.dump(modello_r2_tuple, file)
