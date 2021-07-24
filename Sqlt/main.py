import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create cursor
c = conn.cursor()


# Create table
c.execute("""" CREATE TABLE customers (
        first_name DATATYPE,
        last_name DATATYPE,
        email DATATYPE,
    )""")