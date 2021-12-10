import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/application')
print(engine)

df = pd.read_sql_table('customers',engine)
print(df)

df = pd.read_sql_table('customers', engine, columns=["name"])
print(df)

df = pd.read_sql_query("select id,name from customers",engine)
print(df)

query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''
df = pd.read_sql_query(query,engine)
print(df)

query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''
df = pd.read_sql(query,engine)
print(df)

df = pd.read_sql("customers",engine)
print(df)

df = pd.read_csv("customers.csv")
print(df)

df = df.rename(columns={
    'Customer Name': 'name',
    'Customer Phone': 'phone_number'
}, inplace=True)
print(df)

df = df.to_sql(
    name='customers', # database table name
    con=engine,
    if_exists='append',
    index=False
)
print(df)