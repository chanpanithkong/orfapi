
from ..config.db import db

class tbrolecategories(db.Model):
    
    rolecategoryid = db.Column('rolecategoryid', db.String, primary_key = True)
    rolecategory = db.Column(db.String(255))
    details = db.Column(db.String(255))
    
    def __init__(self, rolecategoryid = None, rolecategory = None, details = None):
        self.rolecategoryid = rolecategoryid
        self.rolecategory = rolecategory
        self.details = details