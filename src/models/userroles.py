from ..config.db import db

class tbuserroles(db.Model):
    
    userid= db.Column('userid', db.String, primary_key = True)
    roleid = db.Column(db.String(10))
    parentid = db.Column(db.String(10))
    status = db.Column(db.Integer)
    details = db.Column(db.String(255))
    
    def __init__(self, userid = None, roleid = None, parentid = None, status = None, details = None):
        self.userid = userid
        self.roleid = roleid
        self.parentid = parentid
        self.status = status
        self.details = details