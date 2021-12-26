Math + ML 
------------
ML: Prediction



1. If a equation is given we can get y for any value of x.  y = f(x)

salary = f(years_of_exp)

y -> salary
x -> years_of_exp

y = f(x) : f(x) =  mx + c 
m- > slope
c -> coeffienc/constant


2. If there are lots of values given for x and y we use sklearn(fit methood) module to derived equation b/w x and y(that it does internally)  so that we can predict y for any given value of x




y ->  salray -> data set 
x --> years_of_exp --> data set

train model follow the syntax


# y/salray is target variable

model = linear_model.LinearRegression()
model.fit(df.x,  df.y) # model.fit(df.years_of_exp,  df.salray)


f(x) =  mx + c 
model.coef_ #slope m
model.intercept_ # intercept/constant c


# predict salary for given experience
--------