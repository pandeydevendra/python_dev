import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv("homeprices.csv")
print(df)

plt.xlabel('area')  # here x >> area
plt.ylabel('price')  # y >> price
plt.scatter(df.area, df.price, color='red', marker='*')
plt.show()
plt.plot(df.area, df.price, color='red', marker='*')
plt.show()

# price is a target value
reg = linear_model.LinearRegression()
reg.fit(df[["area"]], df.price)

# slope[m], interception/costant[c] => y = mx + c
print(reg.coef_, type(reg.coef_))
print(reg.intercept_, type(reg.intercept_))

price = reg.predict([[1000]])
print(price, type(price))

print(reg.predict([[4000]]))

plt.scatter(df.area, df.price, color='red', marker='*')
plt.plot(df.area, reg.predict(df[['area']]), color='blue')
plt.show()
