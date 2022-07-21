from ..config.db import db

class tbsystemserialnumbers(db.Model):
    
    systemid = db.Column('systemid', db.String, primary_key = True)
    serialnumber = db.Column(db.String(10))
    status = db.Column(db.Integer)
    details = db.Column(db.String(255))
    
    
    def __init__(self, systemid = None, serialnumber = None , status = None, details = None):
        self.systemid = systemid
        self.serialnumber = serialnumber
        self.status = status
        self.details = details