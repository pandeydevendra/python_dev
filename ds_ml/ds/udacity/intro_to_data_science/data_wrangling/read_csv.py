# import pandas
#
#
# def add_full_name(path_to_csv, path_to_new_csv):
#     """
#
#     @param path_to_csv:
#     @param path_to_new_csv:
#     @return:
#
#     Assume you will be reading in a csv file with the same columns that the
#     Lahman baseball data set has -- most importantly, there are columns
#     called 'nameFirst' and 'nameLast'.
#     1) Write a function that reads a csv
#     located at "path_to_csv" into a pandas dataframe and adds a new column
#     called 'nameFull' with a player's full name.
#
#     For example:
#       for Hank Aaron, nameFull would be 'Hank Aaron',
#
#     2) Write the data in the pandas dataFrame to a new csv file located at
#     path_to_new_csv
#
#     """
#
#     dataframe = pandas.read_csv(path_to_csv)
#     dataframe['nameFull'] = dataframe['nameFirst'] + ' ' + dataframe['nameLast']
#     dataframe.to_csv(path_to_new_csv)
#
#     # return csv_data, new_csv_data
#
#
# if __name__ == "__main__":
#     # For local use only
#     # If you are running this on your own machine add the path to the
#     # Lahman baseball csv and a path for the new csv.
#     # The dataset can be downloaded from this website: http://www.seanlahman.com/baseball-archive/statistics
#     # We are using the file Master.csv
#     path_to_csv = ("")
#     path_to_new_csv = ("")
#     add_full_name(path_to_csv, path_to_new_csv)
# # Error: file path_to_csv not found....
#
# # Join two 2-D arrays along rows (axis=1): a = [1,2] & b = [3,4] then a+b = [1,2,3,4]
#
# # but adding two array is quite different: a = [1,2] & b = [3,4] then a+b = [4,6]
