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