# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('gfg1.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Creating table
table ="""CREATE TABLE EMPLOYEE(FIRST_NAME VARCHAR(255),
								LAST_NAME VARCHAR(255),
								AGE int,
								SEX CHAR(1),
								INCOME int);"""
cursor.execute(table)
print('Table Created!')

# Queries to INSERT records.
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
					VALUES ('Anand', 'Choubey', 25, 'M', 10000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
					VALUES ('Mukesh', 'Sharma', 20, 'M', 9000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
					VALUES ('Ankit', 'Pandey', 24, 'M', 6300)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
					VALUES ('Subhdra ', 'Singh', 26, 'F', 8000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
					VALUES ('Tanu', 'Mishra', 24, 'F', 6500)''')

print('Data inserted into the table')

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()

# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('gfg1.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Display columns
print('\nColumns in EMPLOYEE table:')
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for column in data.description:
    print(column[0])

# Display data
print('\nData in EMPLOYEE table:')
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()

