import sqlite3
# connect database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor() #create a cursor

# insert data
c.execute("INSERT INTO customers VALUES('rigo', 'lidoli', 'luzolo', 'lit@gmail.com')" )
print("Date Inserted Succesfully !!!!")

# commit our command
conn.commit()
#close connection
conn.close()