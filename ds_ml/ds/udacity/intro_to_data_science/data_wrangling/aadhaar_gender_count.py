import pandas
import pandasql


def aggregate_query(filename):
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = """
    SELECT district, gender, sum(aadhaar_generated)
    FROM aadhaar_data 
    GROUP BY district, gender;"""

    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution


f_name = 'aadhaar_data.csv'
result = aggregate_query(f_name)
print(f"{result}")
