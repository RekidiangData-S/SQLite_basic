import sqlite3
# connect database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor() #create a cursor

many_castomers = [
					('toro', 'polo', 'nzuzi', 'mug@gmail.com'), 
					('zozo', 'lomp', 'mawete', 'pokl@gmail.com'),
					('wolo', 'litp', 'ntonto', 'momo@gmail.com')
				]

# insert data
c.executemany("INSERT INTO customers VALUES(?,?,?,?)", many_castomers)
print("Values Inserted Succesfully !!!!")

# commit our command
conn.commit()
#close connection
conn.close()