from flask import Flask, request
from Answer import Answer
from Question import Question
from db_utils import *

from jwt_utils import build_token

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200


@app.route('/login', methods=['GET', 'POST'])
def Login():
	payload = request.get_json()
	if(payload['password'] == "Vive l'ESIEE !"):
		token = build_token()
		return {"token": str(token)}, 200
	else :
		return '', 401


@app.route('/questions', methods=['GET','POST'])
def PostQuestion():
	if(request.headers.get('Authorization')):
		q1 = Question()
		q1.json_to_object(request.get_json())
		insert_question_into_bd(q1)

		#print("JSON")
		#print(q1.object_to_json())
		#q1.print()
		"""
		a1 = Answer()
		answer = request.get_json()['possibleAnswers']
		for i in range(len(answer)):
			a1.json_to_object(request.get_json(), i)
			#insert_answer_into_bd(a1)
		"""
		
		return '', 200
	else:
		return '', 401

@app.route('/questions/<position>', methods=['GET'])
def GetQuestionNumber(position):
	print("selecting for position")
	if(request.headers.get('Authorization')):
		row = select_questions_with_position(position)
		#print(row)
		#q1 = Question(row[1], row[2], row[0], row[3])
		#jsoned_question = q1.object_to_json()



		return '', 200
	else:
		return '', 401

if __name__ == "__main__":
    app.run(ssl_context='adhoc')