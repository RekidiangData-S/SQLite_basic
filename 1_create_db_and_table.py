import sqlite3
# create data base
#conn = sqlite3.connect(':memory:')  #temporary data base
conn = sqlite3.connect('customer.db')

#create table
c = conn.cursor() #create a cursor
# data type : NULL, INTEGER, REAL, TEXT, BLOB
"""c.execute("""CREATE TABLE customers (
		first_name text,
		name text, 
		last_name text, 
		email text  
	)""")
"""
# insert data
c.execute("INSERT INTO customers VALUES('Reagan', 'Kiese', 'Diangebeni', 'reg@gmail.com')" )

# commit our command
conn.commit()
#close connection
conn.close()