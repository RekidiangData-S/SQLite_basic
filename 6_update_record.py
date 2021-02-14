import sqlite3
# connect database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor() #create a cursor


# Update record

#c.execute("""UPDATE customers SET name ='Rekidiang'
			#WHERE first_name='Reagan'
	#""")

c.execute("""UPDATE customers SET name ='mbuta'
			WHERE rowid=3
	""")

# commit our update
conn.commit()

c.execute("SELECT rowid,* FROM  customers")

#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

for i in c.fetchall():
	print(i)

# commit our command
conn.commit()
#close connection
conn.close()