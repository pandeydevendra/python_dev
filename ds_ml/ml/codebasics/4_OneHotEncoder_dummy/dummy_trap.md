Dummy Variable Trap
When you can derive one variable from other variables, 
they are known to be multi-colinear. 
Here if you know values of california and georgia then you can easily infer value of new jersey state,
i.e. california=0 and georgia=0. 
There for these state variables are called to be multi-colinear. 
In this situation linear regression won't work as expected. Hence you need to drop one column.

NOTE: sklearn library takes care of dummy variable trap 
hence even if you don't drop one of the state columns it is going to work,
however we should make a habit of taking care of dummy variable trap ourselves 
just in case library that you are using is not handling this for you