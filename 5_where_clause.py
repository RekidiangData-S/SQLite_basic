import sqlite3
# connect database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor() #create a cursor

# Qeury the database with where clause
#c.execute("SELECT * FROM  customers WHERE first_name='Reagan'")
#c.execute("SELECT * FROM  customers WHERE rowid=3")
#c.execute("SELECT * FROM  customers WHERE age >=18")
#c.execute("SELECT * FROM  customers WHERE first_name LIKE 'ri%'")
c.execute("SELECT * FROM  customers WHERE first_name LIKE '%ro'")

#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

for i in c.fetchall():
	print(i)

# commit our command
conn.commit()
#close connection
conn.close()