from database import usersTable
import random

def addUser():
	id = random.randint(1,10000)
	name = input('Enter your name, player: ')
	user = (name, id)
	return user
	
