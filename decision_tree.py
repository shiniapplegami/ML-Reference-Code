import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Position_Salaries.csv")
X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
for i in range(0, len(X[0]), 1):
	X[:,i] = le.fit_transform(X[:,i])

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X)

plt.scatter(y, y_pred, color = 'blue')
plt.show()
