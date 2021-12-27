import pandas as pd
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

model = LinearRegression()

ct = ColumnTransformer([('town', OneHotEncoder(), [0])], remainder='passthrough')
df = pd.read_csv("homeprices.csv")
# print(df)

# dummies = pd.get_dummies(df.town)
# print(dummies)

dfle = df
dfle.town = le.fit_transform(dfle.town)
# print(dfle)
x = dfle[['town', 'area']].values
y = dfle.price.values

x = ct.fit_transform(x)
x = x[:, 1:]
# print(x)

model.fit(x, y)
price = model.predict([[1,0,2800]]) # 2800 sqr ft home in robbinsville
print(price)
