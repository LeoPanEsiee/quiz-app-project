# Exemple de création de classe en python
from cgitb import text
import json


class Answer:
    def __init__(self, question_number = 0, text = "", isCorrect = "", answer_number = 0):
        self.question_number = question_number
        self.text = text
        self.isCorrect = isCorrect
        self.answer_number = answer_number

    def json_to_object(self, request_json, indice):
        self.question_number = request_json['position']
        self.text = request_json['possibleAnswers'][indice]['text']
        self.isCorrect = request_json['possibleAnswers'][indice]['isCorrect']
        self.answer_number = indice

    def object_to_json(self):
        return {'text' : self.text, 'isCorrect': self.isCorrect}

    def print(self):
        print(
            "-------------------------" \
            + "\n question_number : " + str(self.question_number) \
            + "\n text : " + self.text \
            + "\n isCorrect : " + str(self.isCorrect) \
            + "\n answer_number : " + str(self.answer_number) \
            + "\n-------------------------"    
            )