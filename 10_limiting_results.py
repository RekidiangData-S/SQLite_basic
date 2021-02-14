import sqlite3
# connect database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor() #create a cursor

# Qeury the database
c.execute("SELECT rowid, * FROM  customers  LIMIT 3")
#c.execute("SELECT rowid, * FROM  customers ORDER BY rowid ASC LIMIT 2")
#c.execute("SELECT rowid, * FROM  customers ORDER BY rowid DESC LIMIT 3")
#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

for i in c.fetchall():
	print(i)

# commit our command
conn.commit()
#close connection
conn.close()