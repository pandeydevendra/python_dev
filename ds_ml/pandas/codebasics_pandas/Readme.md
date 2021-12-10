Different ways of creating 'pandas- dataframe':
1) Using 'CSV'
    pandas.read_csv('file_name.csv')
2) Using 'Excel'
    pandas.read_excel('file_name.excel', engine = 'openpyxl)
3) From python 'dictionary'
    pandas.DataFrame({pass dict})
4) From list of 'tuples'
    pandas.DataFrame((pass tuple))
5) From list of 'dictionary'
    pandas.DataFrame([{},{},{}])



   1) Intro
 * what is pandas? 
 * what using excel/plain python not good. 
 * Show how pandas increase productivity
 
2) Dataframe basics
 * What is dataframe?
 * Dealing with rows and columns
 * Operations: mean, max, std, describe
 * Conditional selection
 * set_index
 
3) Different ways of creating dataframe
 * dictionary, tuples list, list of dictionaries, csv, excel
 
-) reading/writing to excel/csv: http://pbpython.com/excel-pandas-comp.html

-) Handling Missing Data 
 * dropna
 * fillna
 * isnull
 * df.reindex
 
-) Excel Like Operations
 * sort
 * filter
 * remove/rename columns
 * .duplicated 
 * 

-) Selection of data 
 * df['A'] or df.A
 * df[0:3]
 * df['20130102':'20130104']
 * df.loc['Rain'] or df.at['Rain']
 * df.iloc[3]
 * df.iat[1,1]
 * df[df.A > 0]
 

 
-) Merge/Concat/Join
-) Grouping
-) Reshaping/Stack/Unstack
-) Pivot Table
-) Time Series and Categoricals
-) Plotting (Bokeh?)