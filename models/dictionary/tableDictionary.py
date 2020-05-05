from config import db
'''Modelo de crud de ejemplo en React js'''

class tabledictionary(db.Model):
    idWord = db.Column(db.Integer, primary_key=True)
    expression=db.Column(db.String(50))
    definition=db.Column(db.String(150))

    def __init__(self, expression,definition):
        self.expression = expression
        self.definition = definition

