from flask import Flask, request
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
		#q1.print()
		q2 = Question("title2", "this is a question 2", 2, "2x34")
		insert_question_into_bd(q2)
		select_all_questions()

		print("******")
		select_questions_with_title("title2")

		return '', 200
	else:
		return '', 401


if __name__ == "__main__":
    app.run(ssl_context='adhoc')