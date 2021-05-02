import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "root@123", "dev_db")

# prepare a cursor object using cursor() method
#cursor = db.cursor()  # it will give tuple
cursor = db.cursor(MySQLdb.cursors.DictCursor)  # it will give dict..