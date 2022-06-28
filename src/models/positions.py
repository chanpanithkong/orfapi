
from ..config.db import db

class tbpositions(db.Model):
    
    positionid = db.Column('positionid', db.String, primary_key = True)
    position = db.Column(db.String(10))
    details = db.Column(db.String(10))
    
    def __init__(self, positionid = None, position = None, details = None):
        self.positionid = positionid
        self.position = position
        self.details = details