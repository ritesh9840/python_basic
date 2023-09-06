# importing sqlite module
import sqlite3

# create connection to the database
# geeks_database
connection = sqlite3.connect('geeks_database.db')

# insert records into table
connection.execute(
    "INSERT INTO customer_address VALUES (1, 'nikhil teja', 22, 'hyderabad' )")
connection.execute(
    "INSERT INTO customer_address VALUES (2, 'karthik', 25, 'khammam')")
connection.execute(
    "INSERT INTO customer_address VALUES (3, 'sravan', 22, 'ponnur' )")
connection.execute(
    "INSERT INTO customer_address VALUES (4, 'deepika', 25, 'chebrolu' )")
connection.execute(
    "INSERT INTO customer_address VALUES (5, 'jyothika', 22, 'noida')")

# close the connection
connection.close()

# importing sqlite module
import sqlite3

# create connection to the database
# geeks_database
connection = sqlite3.connect('geeks_database.db')

# sql query to display all details from
# table in ascending order based on address.
cursor = connection.execute(
    "SELECT ADDRESS,ID from customer_address ORDER BY address DESC")

# display data row by row
for i in cursor:
    print(i)

# close the connection
connection.close()

# importing sqlite module
import sqlite3

# create connection to the database
# geeks_database
connection = sqlite3.connect('geeks_database.db')

# sql query to display address and id
# based on address in descending order
cursor = connection.execute(
    "SELECT ADDRESS,ID from customer_address ORDER BY address DESC")

# display data row by row
for i in cursor:
    print(i)

# close the connection
connection.close()

# importing sqlite module
import sqlite3

# create connection to the database
# geeks_database
connection = sqlite3.connect('geeks_database.db')

# sql query to display name and id based
# on name in descending order
cursor = connection.execute(
    "SELECT NAME,ID from customer_address ORDER BY NAME DESC")

# display data row by row
for i in cursor:
    print(i)

# close the connection
connection.close()