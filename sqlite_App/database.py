import sqlite3

def create_db():
	conn = sqlite3.connect('customer.db')
	#create table
	c = conn.cursor() #create a cursor
	# data type : NULL, INTEGER, REAL, TEXT, BLOB

	c.execute("""CREATE TABLE customers (
			first_name text,
			last_name text, 
			age text, 
			phone_number text  
		)""")

def show_all():
	"""
		Query the DB and return all records
	"""
	print("************ ALL RECORDS ************************")
	
	#create DB or Connect to DB
	conn = sqlite3.connect('customer.db')
	#create a cursor
	c = conn.cursor() 

	# Qeury the database
	c.execute("SELECT rowid, * FROM  customers")
	items = c.fetchall()

	for i in items:
		print(i)

	# commit our command
	conn.commit()
	#close connection
	conn.close()

def add_one(first_name, last_name, age, phone_number):
	"""
		Add new record to the table
	"""
	#create DB or Connect to DB
	conn = sqlite3.connect('customer.db')
	#create a cursor
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES(?,?,?,?)", (first_name, last_name, age, phone_number))
	# commit our command
	conn.commit()
	#close connection
	conn.close()

def add_record():
	print("Add New Record :")
	print("*************** :")
	first_name = input("Enter First Name : ")
	last_name = input("Enter Last Name : ")
	age = input("Enter Age : ")
	phone_number = input("Enter Phone Number : ")
	
	print("************************************")
	print("New Record Added Succesfully !!!")
	add_one(first_name, last_name, age, phone_number)

def delete_one(id):
	"""
		delete record from the table
	"""
	#create DB or Connect to DB
	conn = sqlite3.connect('customer.db')
	#create a cursor
	c = conn.cursor()
	print("DELETE RECORD")
	print("*************")
	print("Which Record do you want to delete () : ")
	id = input("Enter Record Id : ")
	
	mem = input("Do you want to delete this record(Yes/No) :")
	if mem == 'Yes':
		c.execute("DELETE FROM customers WHERE rowid = (?)",id)
		print("Record deleted succesfully!!")
	else:
		print("Delete operation canceled !!")
	# commit our command
	conn.commit()
	#close connection
	conn.close()

def selection(attribut, cle):
	"""
		Select record using WHERE
	"""

	#create DB or Connect to DB
	conn = sqlite3.connect('customer.db')
	#create a cursor
	c = conn.cursor()

	c.execute("SELECT rowid, * from customers WHERE attribut = (?)", (cle,))

	for i in items:
		print(i)
	# commit our command
	conn.commit()
	#close connection
	conn.close()
def select():
	attribut = input("Enter Attribut :")
	cle = input("Enter Cle :")
	selection(attribut, cle)