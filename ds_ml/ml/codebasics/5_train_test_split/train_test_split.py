import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

"""
Out of population 'p',
select sample 's' to train the model 
and keep rest of the data o test , how better the accuracy of the system is.
"""

df = pd.read_csv("carprices.csv")
# print(df.head())

X = df[['Mileage','Age(yrs)']]
y = df['Sell Price($)']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
# print(X_train)

from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train, y_train)
# print(clf.predict(X_test))
print(clf.score(X_test, y_test))

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)
print(X_test)