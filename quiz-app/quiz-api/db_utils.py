import sqlite3
from Answer import Answer

from Question import Question


def insert_question_into_bd(question):
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    cur.execute(
	f"insert into question (title, text, position, image) values"
	f"( \"{question.title}\", \"{question.text}\", \"{question.position}\", \"{question.image}\")")

    cur.execute("commit")

def insert_answer_into_bd(answer):
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    cur.execute(
    f"insert into answer (question_number, text, isCorrect, answer_number) values"
    f"( \"{answer.question_number}\", \"{answer.text}\", \"{answer.isCorrect}\", \"{answer.answer_number}\")")

    cur.execute("commit")


"""
def select_all_questions():
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    select_result = cur.execute("select * from question")
    output = select_result.fetchall()
    for row in output:
        print(row)


def select_questions_with_title(title):
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    select_result = cur.execute(f"select * from question where title = \"{title}\"")

    output = select_result.fetchall()
    for row in output:
        print(row)
"""


"""Select the question and its answers from the database
Returns the json of the entire question with its answers

"""
def select_question_with_position(position):
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    #Database request should only give 1 result
    select_questions_result = cur.execute(f"select * from question where position = {position}")
    output = select_questions_result
    for row in output:
        #Create the question from the database values
        q1 = Question(row[1], row[2], row[0], row[3])

    #make sure the list is empty
    q1.possibleAnswers.clear()
    
    #Database requesting all answers associated with the question's position
    select_questions_result = cur.execute(f"select * from answer where question_number = {position}")
    output = select_questions_result.fetchall()
    for col in output:
        a1 = Answer(0, col[1], col[2], 0)
        q1.possibleAnswers.append(a1.object_to_json())

    
    return q1.object_to_json()

    
    



    
    
