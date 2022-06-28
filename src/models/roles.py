
from ..config.db import db

class tbroles(db.Model):
    
    roleid = db.Column('roleid', db.String, primary_key = True)
    role = db.Column(db.String(100))
    rolecategoryid = db.Column(db.String(5))
    details = db.Column(db.String(255))

    def __init__(self, roleid = None, role = None, rolecategoryid = None, details = None):
        self.roleid = roleid
        self.role = role
        self.rolecategoryid = rolecategoryid
        self.details = details