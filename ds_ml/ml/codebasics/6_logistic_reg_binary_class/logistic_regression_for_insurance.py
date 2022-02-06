"""
Objective: Train a model to predict whether a person would buy an insurance or not,
(Yes/No: Binary Classification type)
Features: age (single variable)
"""
# import all desired libraries:
import pandas as pd
import numpy as np
import seaborn as sn
import math
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# read model data to create a dataframe:

df = pd.read_csv('insurance_data.csv')
print(df)
print(f"DataFrame info:")
print(f"{df.info()}")
print(f"Null values in DataFrame:\n {df.isnull().sum()}")
plt.scatter(df.age, df.bought_insurance, marker='*', color='b')
plt.show()

# split dataset into two prats >> train(90%), test(10%) >> test_size = 0.1 or train_size = 0.9:

x_train, x_test, y_train, y_test = train_test_split(df[['age']], df['bought_insurance'], test_size=.1)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

# train your model by obtaining an object > log_reg_model:
log_reg_model = LogisticRegression()
print(f"{log_reg_model}, {type(log_reg_model)}")

log_reg_model.fit(x_train, y_train)

# predict the result:
y_predicted = log_reg_model.predict(x_test)
print(y_predicted)
print(y_test)

df_yp = pd.DataFrame(y_predicted, columns=['prediction'])
print(df_yp)
combine = [df['age'], df['bought_insurance'], df_yp['prediction']]
column_name = ["age", "bought_insurance", "prediction"]
df_predicted = pd.concat(combine, axis=1, keys=column_name)
print(df_predicted)
print(df_predicted.head(len(x_test)))

# check for accuracy of the model:
score = log_reg_model.score(x_train, y_train)
print(f"Accuracy of the model = {score * 100}%")
proba = log_reg_model.predict_proba(x_test)
print(f"probability : {proba}")
print(f"coeff: {log_reg_model.coef_}, intercept: {log_reg_model.intercept_}")
print(f"coeff_type: type{type(log_reg_model.coef_)}, intercept: {type(log_reg_model.intercept_)}")

cm = confusion_matrix(y_test, y_predicted)
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()
