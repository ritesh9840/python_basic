# Complete python program to get
# the total no. of change since the
# beginning of the database connection.

# Import sqlite3 module to work with
# SQLite using python.
import sqlite3

# Create connection object by connecting
# to the required database (here geeks.db)
con = sqlite3.connect('geeks.db')

# SQL string to Create a database table
# named person.
create_table = '''CREATE TABLE person(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
				age INTEGER NOT NULL
				);'''

# Execute the above SQL query.
con.execute(create_table)

# Print the current total no. of changes.
print("Total changes initially:")
print(f'total_changes = {con.total_changes}\n')

# SQL string to insert records into
# the table named person.
insert_data = '''INSERT INTO person(name, age)
				VALUES ("Yogesh",21),
				("Vishal", 22),
				("Ajit",22),
				("Ashish",21),
				("Tanvi", 20);'''

# Execute the above SQL query.
con.execute(insert_data)

# Print the current total no. of changes.
print("Total changes after inserting 5 rows:")
print(f'total_changes = {con.total_changes}\n')

# SQL string to Select (retrieve) records
# from a database table named person.
select_data = 'SELECT * FROM person;'

# Execute the above SQL query.
cursor = con.execute(select_data)

# Create a list of column names of the
# database table named person.
header = [d[0] for d in cursor.description]

# Print the column names separated
# by a single space.
print(*header)

# Print the retrieved data.
for row in cursor:
    print(*row)
print()

# SQL string to delete a record from a
# database table named person.
delete_data = 'DELETE FROM person WHERE name="Tanvi";'

# Execute the above SQL query.
con.execute(delete_data)

# Print the current total no. of changes.
print("Total changes after deleting a row:")
print(f'\ntotal_changes = {con.total_changes}\n')

# Retrieve the modified (here deleted
# one record/row) data from a database
# table named person.
cursor = con.execute('SELECT * FROM person;')

# Print the retrieved data.
print(*header)
for row in cursor:
 print(*row)
print()

# Commit the changes to persist the
# changes.
con.commit()

# Close the database connection.
con.close()
