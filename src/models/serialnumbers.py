from ..config.db import db

class tbserialnumbers(db.Model):
    
    serialnumber = db.Column('serialnumber', db.String, primary_key = True)
    formname = db.Column(db.String(255))
    details = db.Column(db.String(255))
    
    def __init__(self, serialnumber = None, formname = None , details = None):
        self.serialnumber = serialnumber
        self.formname = formname
        self.details = details