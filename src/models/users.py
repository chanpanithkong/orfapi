from ..config.db import db

class tbusers(db.Model):
    
    userid= db.Column('userid', db.String, primary_key = True)
    password = db.Column(db.String(255))
    lastname = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    gender = db.Column(db.String(40))
    branchcode = db.Column(db.String(4))
    email = db.Column(db.String(255))
    phonenumber = db.Column(db.String(20))
    address = db.Column(db.String(255))
    deptid = db.Column(db.String(10))
    positionid = db.Column(db.String(10))
    
    def __init__(self, userid = None, password = None, lastname = None, firstname = None, gender = None, branchcode = None, email = None, phonenumber = None, address = None, deptid = None, positionid = None):
        self.userid = userid
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.branchcode = branchcode
        self.email = email
        self.phonenumber = phonenumber
        self.address = address
        self.deptid = deptid
        self.positionid = positionid

    @classmethod
    def find_by_userid(cls, userid) -> "tbusers":
        return cls.query.filter_by(userid=userid).first()

        

    