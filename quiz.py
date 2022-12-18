
score = 0

def creatChoiceDict(a,b,c,d):
	dict = {'a':a,'b':b,'c':c,'d':d}
	return dict

def getAnswer(choiceDict, correct):
	for key in choiceDict:
		print(f'{key.upper()}: {choiceDict[key]}')

	answer = input("\nYour answer: ")

	print(f"You chose {choiceDict[answer.lower()]}\n")

	if answer.lower() == correct:
		print("You are correct!\n")
		return True
	else:
		print(f"You are incorrect. The correct answer is {choiceDict[correct]}\n")
		return False

def printScore():
	dec = "************************************************"
	print(dec)
	print(f"SCORE: {score}")
	print(dec)
	print('\n')

def adjustScore(answer):
	global score
	if answer is True:
		score = score + 10
	else:
		score = score-10
	printScore()

def q1():
	print('Who is the director of "Mad Men"?')
	choiceDict = creatChoiceDict('Jake', 'Will', 'Hamm', 'Leo')
	answer = getAnswer(choiceDict, 'c')
	adjustScore(answer)

def q2():
	print('Who started Honda?')
	choiceDict = creatChoiceDict('Honda', 'Seiji', 'Mibe', 'Chan')
	answer = getAnswer(choiceDict, 'a')
	adjustScore(answer)	

def q3():
	print('What is the oldest volcano?')
	choiceDict = creatChoiceDict('Vesuvius', 'Etna', 'Pompey', 'Fuji')
	answer = getAnswer(choiceDict,'b')
	adjustScore(answer)
	
q1()
q2()
q3()