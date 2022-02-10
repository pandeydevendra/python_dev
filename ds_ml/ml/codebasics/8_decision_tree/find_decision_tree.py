import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
df = pd.read_csv("salaries.csv")
print(df.head())

X = df.drop('salary_more_then_100k', axis='columns')
y = df['salary_more_then_100k']

LblEncd_company = LabelEncoder()
LblEncd_job = LabelEncoder()
LblEncd_degree = LabelEncoder()

print(X.info())
X['company_num'] = LblEncd_company.fit_transform(X['company'])
X['job_num'] = LblEncd_job.fit_transform(X['job'])
X['degree_num'] = LblEncd_degree.fit_transform(X['degree'])

print(X)

X_num = X.drop(['company','job','degree'], axis='columns')
print(X_num)
print(y)


dczn_tree_model = tree.DecisionTreeClassifier()
print(dczn_tree_model)

dczn_tree_model.fit(X_num, y)

score = dczn_tree_model.score(X_num, y)
print(score)

# Salary > 100 k ? Yes(1) or No(0)

print(dczn_tree_model.predict([[0,0,0]]))
print(dczn_tree_model.predict([[1,1,1]]))
print(dczn_tree_model.predict([[2,2,2]]))
print(dczn_tree_model.predict([[3,3,0]]))
print(dczn_tree_model.predict([[2,1,1]]))
print(dczn_tree_model.predict([[2,3,1]]))
print(dczn_tree_model.predict([[2,4,1]]))