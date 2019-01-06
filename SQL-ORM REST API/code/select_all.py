import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

print "*** USERS *** "
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
	print(row)

print "*** ITEMS *** "
select_query = "SELECT * FROM items"
for row in cursor.execute(select_query):
	print(row)