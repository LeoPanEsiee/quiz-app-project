# Exemple de création de classe en python
from cgitb import text
import json


class Question:
    def __init__(self, title = "", text = "", position = 0, image = ""):
        self.title = title
        self.text = text
        self.position = position
        self.image = image

    def json_to_object(self, json_object_payload):
        self.text = json_object_payload['text']
        self.title = json_object_payload['title']
        self.image = json_object_payload['image']
        self.position = json_object_payload['position']

    def object_to_json(self):
        return {'text' : self.text, 'title': self.title, 'image' : self.image, 'position' : self.position}

    def print(self):
        print(
            "-------------------------" \
            + "\n text : " + self.text \
            + "\n title : " + self.title \
            + "\n image : " + self.image \
            + "\n position : " + str(self.position) \
            + "\n-------------------------"    
            )