from ..config.db import db

class tbsystems(db.Model):
    
    systemid = db.Column('systemid', db.String, primary_key = True)
    systemname = db.Column(db.String(150))
    details = db.Column(db.String(255))
    
    def __init__(self, systemid = None, systemname = None, details = None):
        self.systemid = systemid
        self.systemname = systemname
        self.details = details