import sqlite3
# connect database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor() #create a cursor

#c.execute("SELECT * FROM  customers WHERE first_name LIKE '%ro' AND rowid=6")
#c.execute("SELECT * FROM  customers WHERE first_name LIKE '%ro' OR rowid=6")
c.execute("SELECT * FROM  customers WHERE first_name LIKE '%ro' OR rowid=6 OR first_name='zozo'")

#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

for i in c.fetchall():
	print(i)

# commit our command
conn.commit()
#close connection
conn.close()