import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn
import seaborn as sb

from sklearn import linear_model

excel_file = pd.ExcelFile("chegg17_04_21.xlsx")  # filename as file name of excel data sheet
print(excel_file.filename)

df = excel_file.parse('x_y')  # x= variable1 (input), y= variable2(output)
print(df)

plt.xlabel('x')
plt.ylabel('y')

plt.scatter(df.x, df.y, color='blue', marker='.')

df_x = pd.DataFrame(df.x)

reg = linear_model.LinearRegression()
reg.fit(df_x, df_y)
print(reg.coef_, reg.intercept_)
print(reg.predict([[xn]]))  # xn = any value of x to predict corresponding yn
