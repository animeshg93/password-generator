from database import questionsTable, usersTable

score = 0

def creatChoiceDict(list):
	dict = {'a':list[0],'b':list[1],'c':list[2],'d':list[3]}
	return dict


def getAnswer(choiceDict, correctAnswer):
	for key in choiceDict:
		print(f'{key.upper()}: {choiceDict[key]}')

	answer = input("\nYour answer: ")

	print(f"You chose {choiceDict[answer.lower()]}\n")

	if choiceDict[answer.lower()] == correctAnswer:
		print("You are correct!\n")
		return True
	else:
		print(f"You are incorrect. The correct answer is {correctAnswer}\n")
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


def questions():
	for i in range(1,4):
		questionID = {'QUESTION': 'QUESTION#','ID': '00'+ str(i)}

		questionObject = questionsTable.get_item(Key=questionID)['Item']
		question = questionObject['Question']
		
		print(question+"\n")
		choiceDict = creatChoiceDict(questionObject['Choices'])
		answer = getAnswer(choiceDict, questionObject['CorrectAnswer'])
		adjustScore(answer)

questions()