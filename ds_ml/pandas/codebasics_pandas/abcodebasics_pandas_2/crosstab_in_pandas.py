import pandas as pd
import numpy as np

df = pd.read_excel("survey.xlsx", engine="openpyxl")
print(df)

df1 = pd.crosstab(df.Nationality,df.Handedness)
print(df1)

df2 = pd.crosstab(df.Sex,df.Handedness)
print(df2)

df3 = pd.crosstab(df.Sex,df.Handedness, margins=True)
print(df3)

df4 = pd.crosstab(df.Sex, [df.Handedness,df.Nationality], margins=True)
print(df4)

df5 = pd.crosstab([df.Nationality, df.Sex], [df.Handedness], margins=True)
print(df5)

df6 = pd.crosstab(df.Sex, df.Handedness, normalize='index')
print(df6)

df7 = pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average)
print(df7)
