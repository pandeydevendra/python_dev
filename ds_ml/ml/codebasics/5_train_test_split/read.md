Training And Testing Available Data

We have a dataset containing prices of used BMW cars. 
We are going to analyze this dataset and build a prediction function 
that can predict a price by taking mileage and age of the car as input. 
We will use sklearn train_test_split method to split training and testing dataset

Looking at above two scatter plots,
using linear regression model makes sense as we can clearly
see a linear relationship between our dependant (i.e. Sell Price) and
independant variables (i.e. car age and car mileage)

The approach we are going to use here is to split available data in two sets

Training: We will train our model on this dataset
Testing: We will use this subset to make actual predictions using trained model

The reason we don't use same training set for testing is because our model has seen those samples before,
using same samples for making predictions might give us wrong impression about accuracy of our model. 
It is like you ask same questions in exam paper as you tought the students in the class.