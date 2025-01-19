from ...config.database import db, BaseModel
from flask import url_for

class Alphabet(BaseModel):
    __tablename__ = 'alphabets'

    name = db.Column(db.String(255), nullable=False)
    slug_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.Text(), nullable=False)
    
    #constructor
    # def __init__(self, parent_id=None, email=None, password=None):
    #     self.name = name
    #     self.email = email
    #     self.authenticated = True
    
    def jsonResponse(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': url_for('static', filename='storage/alphabets/'+self.image)
        }