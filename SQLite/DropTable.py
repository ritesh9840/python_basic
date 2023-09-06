# importing sqlite module
import sqlite3

# create connection to the
# database geek
connection = sqlite3.connect('geeks_database.db')

# drop table
connection.execute("DROP TABLE customers_address")

print("data dropped successfully")

# close the connection
connection.close()
