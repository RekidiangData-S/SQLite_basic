import sqlite3
# connect database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor() #create a cursor


# Delete record

#
print(f"DataBase Size : {len(c.fetchall())}")

rec = input("Which Record do you want to delete (Enter Record Id) : ")
mem = input("Do you want to delete this record(Yes/No) :")
print(type(rec))
print(type(2))

if mem == 'Yes':
	c.execute("DELETE from customers WHERE rowid=rec")
else:
	print("Delete operation canceled !!")

# commit our update
conn.commit()

c.execute("SELECT rowid,* FROM  customers")

#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

for i in c.fetchall():
	print(i)
print(f"DataBase Size : {len(c.fetchall())}")

# commit our command
conn.commit()
#close connection
conn.close()