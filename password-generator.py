from random import randint as rand
import random as random
import string as string

numbers = int(input("Enter number of numbers: "))
letters = int(input("Enter number of letters: "))

list_of_letters = string.ascii_letters
answer= ""

while numbers+letters > 0:
	choice = rand(0,10)
	if choice <5 :
		answer += str(rand(0,10))
		numbers -= 1
	else:
		answer +=random.choice(list_of_letters)
		letters -=1 

print("Your password is: %s" %answer)