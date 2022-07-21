from ..config.db import db

class tbuserrequestforms(db.Model):
    
    aid= db.Column('aid', db.String, primary_key = True)
    formid = db.Column(db.String(10))
    formcategoryid = db.Column(db.Integer)
    serialnumber = db.Column(db.String(10))
    fieldname = db.Column(db.String(255))
    fieldvalue = db.Column(db.String(255))
    userid = db.Column(db.String(10))
    
    
    def __init__(self, aid = None, formid = None, formcategoryid = None, serialnumber = None, fieldname = None, fieldvalue = None, userid = None):
        self.aid = aid
        self.formid = formid
        self.formcategoryid = formcategoryid
        self.serialnumber = serialnumber
        self.fieldname = fieldname
        self.fieldvalue = fieldvalue
        self.userid = userid