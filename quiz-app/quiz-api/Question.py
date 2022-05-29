# Exemple de création de classe en python
from asyncio.windows_events import NULL
from cgitb import text
import json
from Answer import Answer


class Question:
    def __init__(self, title = "", text = "", position = 0, image = "", possibleAnswers = []):
        self.title = title
        self.text = text
        self.position = position
        self.image = image
        self.possibleAnswers = possibleAnswers

    def json_to_object(self, request_json):
        self.text = request_json['text']
        self.title = request_json['title']
        self.image = request_json['image']
        self.position = request_json['position']
        
        a1 = Answer()
        for i in range(len(request_json['possibleAnswers'])):
            a1.json_to_object(request_json, i)
            self.possibleAnswers.append({ "text" : a1.text, "isCorrect" : a1.isCorrect })
            

    def object_to_json(self):
        return {"text" : self.text, "title": self.title, "image" : self.image, "position" : self.position , "possibleAnswers" : self.possibleAnswers}

    def print(self):
        print(
            "-------------------------" \
            + "\n text : " + self.text \
            + "\n title : " + self.title \
            + "\n image : " + self.image \
            + "\n position : " + str(self.position) \

            + "\n-------------------------"    
            )
        
        