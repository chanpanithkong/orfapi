from flask import Flask
from ..config.db import db

class tbstatus(db.Model):
    
   statusid = db.Column('statusid', db.Integer, primary_key = True)
   status = db.Column(db.String(100))
   details = db.Column(db.String(255))

   def __init__(self, statusid = None, status = None, details = None):
    self.statusid = statusid
    self.status = status
    self.details = details

#     def create(self):
#         db.session.add(self)
#         db.session.commit()
#         return self


# db.create_all()