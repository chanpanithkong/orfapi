from ..config.db import db

class tbuserlogs(db.Model):
    
    userlogid = db.Column('userlogid', db.String, primary_key = True)
    activity = db.Column(db.String(150))
    createddate = db.Column(db.String)
    createdby = db.Column(db.String(10))
    
    
    def __init__(self, userlogid = None, activity = None , createddate = None, createdby = None):
        self.userlogid = userlogid
        self.activity = activity
        self.createddate = createddate
        self.createdby = createdby