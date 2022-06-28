from ..config.db import db

class tbformcategories(db.Model):
    
    formcategoryid = db.Column('formcategoryid', db.String, primary_key = True)
    formcategory = db.Column(db.String(200))
    details = db.Column(db.String(255))
    
    def __init__(self, formcategoryid = None, formcategory = None, details = None):
        self.formcategoryid = formcategoryid
        self.formcategory = formcategory
        self.details = details