from asyncio.windows_events import NULL
import sqlite3

def insert_question_into_bd(question):
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    question.print()

    cur.execute(
	f"insert into question (title, text, position, image) values"
	f"( \"{question.title}\", \"{question.text}\", \"{question.position}\", \"{question.image}\")")

    cur.execute("commit")

def insert_answer_into_bd(answer):
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    answer.print()

    cur.execute(
    f"insert into answer (question_number, text, isCorrect, answer_number) values"
    f"( \"{answer.question_number}\", \"{answer.text}\", \"{answer.isCorrect}\", \"{answer.answer_number}\")")

    
    cur.execute("commit")



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

def select_questions_with_position(position):
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    select_result = cur.execute(f"select * from question inner join answer on question.position = answer.question_number where position = {position}")

    output = select_result.fetchall()

    for row in output:
        print(row)

def delete_question_with_position(position):
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    select_result = cur.execute(f"SELECT title FROM question WHERE position = {position}")
    output = select_result.fetchall()

    if(output != []):
        cur.execute(f"DELETE FROM question WHERE position = {position}")
        cur.execute(f"DELETE FROM answer WHERE question_number = {position}")
        cur.execute("commit")
        return True
    else:
        return False





    
    
