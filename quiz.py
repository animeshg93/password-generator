
score = 0

def getAnswer(a,b,c,d, correct):
	print(f"A: {a}\nB: {b}\nC: {c}\nD: {d}")
	answer = input("\nYour answer: ")
	option = ''
	match answer.casefold():
		case "a":
			print(f'You chose {a}\n')
			option = a
		case "b":
			print(f'You chose {b}\n')
			option = b
		case "c":
			print(f'You chose {c}\n')
			option = c
		case "d":
			print(f'You chose {d}\n')
			option = d

	if option == correct:
		print("You are correct!\n")
		return True
	else:
		print(f"You are incorrect. The correct answer is {correct}\n")
		return False

def printScore():
	dec = "************************************************"
	print(dec)
	print(f"SCORE: {score}")
	print(dec)

def adjustScore(answer):
	global score
	if answer is True:
		score = score + 10
	else:
		score = score-10
	printScore()

def q1():
	print('Who is the director of "Mad Men"?')
	a = "Jake"
	b = "Will Smith"
	c = "Jon Hamm"
	d = "Leo Caprio"
	answer = getAnswer(a,b,c,d,c)
	adjustScore(answer)

def q2():
	print('Who started Honda?')
	a = "Honda Soichiro"
	b = "Seiji Kuraishi"
	c = "Toshihiro Mibe"
	d = "Jackie Chan"
	answer = getAnswer(a,b,c,d,a)
	adjustScore(answer)	

def q3():
	print('What is the oldest volcano?')
	a = "Vesuvius"
	b = "Etna"
	c = "Fuji"
	d = "Pompey"
	answer = getAnswer(a,b,c,d,b)
	adjustScore(answer)
	
q1()
q2()
q3()