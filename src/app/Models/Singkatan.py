from ...config.database import db, BaseModel
from flask import url_for

class Singkatan(BaseModel):
    __tablename__ = 'singkatans'

    #table columns
    singkatan = db.Column(db.String(255), nullable=False)
    kepanjangan = db.Column(db.String(255), nullable=False)
    
    #constructor
    # def __init__(self, parent_id=None, email=None, password=None):
    #     self.name = name
    #     self.email = email
    #     self.authenticated = True
    
    def jsonResponse(self):
        return {
            'id': self.id,
            'singkatan': self.singkatan,
            'kepanjangan': self.kepanjangan
        }