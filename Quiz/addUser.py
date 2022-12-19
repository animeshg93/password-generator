from database import usersTable

id = 100

def addUser():
	global id

	name = input('Enter your name, player: ')
	user = (name, id)
	id += 1
	return user
	
