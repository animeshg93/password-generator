from database import questionsTable
from utilities import *


def quiz():
	for i in range(100,103):
		questionID = {'QUESTION': 'QUESTION#','ID': str(i)}
		questionObject = questionsTable.get_item(Key=questionID)['Item']
		question = questionObject['Question']
		
		print(question+"\n")
		choiceDict = creatChoiceDict(questionObject['Choices'])
		answer = getAnswer(choiceDict, questionObject['CorrectAnswer'])
		adjustScore(answer[0])
		updateUserScore(questionObject, answer)
		
	printScore()	
	updateUserFinalScore()

quiz()