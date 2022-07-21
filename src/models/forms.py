from ..config.db import db

class tbforms(db.Model):
    
    formid = db.Column('formid', db.String, primary_key = True)
    formcategoryid = db.Column(db.String(10))
    serialnumber = db.Column(db.String(10))
    fieldname = db.Column(db.String(255))
    fieldcontroller = db.Column(db.Integer)
    status = db.Column(db.Integer)
    
    def __init__(self, formid = None, formcategoryid = None, serialnumber = None, fieldname = None, fieldcontroller = None, status = None):
        self.formid = formid
        self.formcategoryid = formcategoryid
        self.serialnumber = serialnumber
        self.fieldname = fieldname
        self.fieldcontroller = fieldcontroller    
        self.status = status