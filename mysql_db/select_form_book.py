from dev_db import cursor, db

sql_query = "SELECT * FROM book"
cursor.execute(sql_query)
books = cursor.fetchall()
print(books)
print(type(books))

for book in books:
    # print(book, type(book))
    print("the price of {} is {}.".format(book['title'], book['price']))
db.close()