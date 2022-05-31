import json
from Answer import Answer

class Participation:
    """Participation constructor
        values can be null
        takes params : player_name : le nom du joueur qui poste son questionnaire
        answers : la liste des positions de réponses choisies dans l’ordre des questions du quiz
    """
    def __init__(self, playerName = "", answers = []):
        self.playerName = playerName
        self.answers = answers

    
    """Put the json data into the python Participation
    """
    def json_to_object(self, request_json):
        self.playerName = request_json['playerName']
        self.answers = request_json['answers']


    """Returns the json version of the Participation
    """
    def object_to_json(self):
        """
        answersSummaries : [
        {
            correctAnswerPosition : 2,
            wasCorrect : true
        },
        {
            correctAnswerPosition : 1,
            wasCorrect : false
        },....

        {
            correctAnswerPosition : 3,
            wasCorrect : true
        }
        ],
        playerName : "Anton",
        score : 4
        """
        return data_json

    def print(self):
        print(
            "-------------------------" \
            + "\n playerName : " + self.playerName \
            + "\n answers : " + str(self.answers) \
            + "\n-------------------------"    
            )
