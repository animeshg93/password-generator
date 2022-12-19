import boto3

dynamodb = boto3.resource('dynamodb')
questionsTable = dynamodb.Table('Questions')
usersTable = dynamodb.Table('Quiz-Users')

# print(table.creation_date_time)

