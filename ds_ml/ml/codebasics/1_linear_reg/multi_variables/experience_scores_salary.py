import pandas as pd
import numpy as np
from sklearn import linear_model
import math
from word2number import w2n

df = pd.read_csv('hiring.csv')
print(df)
df.experience = df.experience.fillna('zero')
test_score_fill = math.floor(df['test_score(out of 10)'].mean())
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(test_score_fill)
print(df)
df.experience = df.experience.apply(w2n.word_to_num)
print(df)

reg = linear_model.LinearRegression()

reg.fit(df[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']], df['salary($)'])

print(reg.predict([[2, 9, 6]]))
print(reg.predict([[12, 10, 10]]))
print(reg.predict([[1, 10, 10]]))
