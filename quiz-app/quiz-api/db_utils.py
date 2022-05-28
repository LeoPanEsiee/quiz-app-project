import sqlite3

def insert_question_into_bd(question):
    db_connection = sqlite3.connect('../quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    question.print()

    insertion_result = cur.execute(
	f"insert into question (title, text, position, image) values"
	f"( \"{question.title}\", \"{question.text}\", \"{question.position}\", \"{question.image}\")")

    #print (insertion_result)
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

    select_result = cur.execute(f"select * from question where position = {position}")

    output = select_result.fetchall()

    for row in output:
        return row


    
    
