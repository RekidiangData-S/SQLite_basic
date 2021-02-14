import database

#database.create_db()
def main():

	print(""" 
		WELCOME TO STUDENTS DATABASE
		############################
		Select Operation :
		(1) for create Table
		(2) for Add Record
		(3) for Show Records
		(4) for Delete Records
		(5) for Records Selection
		""")
	operation = input("Enter your Choice : ")
	if operation == "2":
		database.add_record()
	elif operation == "3":
		database.show_all()
	elif operation == "4":
		database.delete_one(id)
	elif operation == "5":
		database.select()
	elif operation == "1":

		print("Please Contact DataBase Admonistrator for this Operation")
	else:
		print("Try again !!")




	



main()
#database.add_record()
#database.show_all()
#database.delete_one(id)