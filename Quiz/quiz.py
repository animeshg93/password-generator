from database import questionsTable, usersTable
from addUser import addUser

user = addUser()
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
		return (True, choiceDict[answer.lower()])
	else:
		print(f"You are incorrect. The correct answer is {correctAnswer}\n")
		return (False, choiceDict[answer.lower()])


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

def updateUserScore(questionObject, answer):
	usersTable.put_item(
		Item={
        'Name': user[0],
        'QuestionID': questionObject['ID'],
        'UserID': str(user[1]),
        'IsCorrect': answer[0],
        'Answer': answer[1]
    })


def questions():
	for i in range(100,103):
		questionID = {'QUESTION': 'QUESTION#','ID': str(i)}
		questionObject = questionsTable.get_item(Key=questionID)['Item']
		question = questionObject['Question']
		
		print(question+"\n")
		choiceDict = creatChoiceDict(questionObject['Choices'])
		answer = getAnswer(choiceDict, questionObject['CorrectAnswer'])
		adjustScore(answer[0])
		updateUserScore(questionObject, answer)

questions()