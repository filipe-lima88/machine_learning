import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
# y_pred = regressor.predict(X_test)
#salva o modelo
pickle.dump(regressor, open('modelo.pkl','wb'))

# model = pickle.load(open('modelo.pkl','rb'))
# print(model.predict([[1.8]]))