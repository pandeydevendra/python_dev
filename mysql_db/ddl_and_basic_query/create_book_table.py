from dev_db import cursor, db

#this is for testing purpose only, we will create table using mysql directly.

create_table_query ="CREATE TABLE IF NOT EXISTS book_test(id int(4), title varchar(20), price float(5, 2))"
cursor.execute(create_table_query)
