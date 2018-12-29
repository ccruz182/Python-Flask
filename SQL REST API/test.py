import sqlite3

connection = sqlite3.connect('data.db')

# Allows to select things
cursor = connection.cursor()

# Creation of the query. Creating a table
create_table = "CREATE TABLE users (id int, username text, password text)"

# Execution of the query
cursor.execute(create_table)

# Inserting data to the db
user = (1, 'Cesar', '1234')
users_list = [
	(2, 'Joel', '0000'),
	(3, 'Jose', 'qwerty')
]
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)
cursor.executemany(insert_query, users_list)

# Save all changes
connection.commit()

# Retrieve data from db
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
	print(row)


# Close the actual connection. Not consuming more resources
connection.close()
