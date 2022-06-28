from ..config.db import db

class tbdepts(db.Model):
    
    deptid = db.Column('deptid', db.String, primary_key = True)
    deptcode = db.Column(db.String(20))
    departments = db.Column(db.String(200))
    
    def __init__(self, deptid = None, deptcode = None, departments = None):
        self.deptid = deptid
        self.deptcode = deptcode
        self.departments = departments