
from .BaseModel import BaseModel
from ...config.database import db

class Category(BaseModel):
    __tablename__ = 'categories'

    parent_id = db.Column(db.BigInteger, nullable=True)
    name = db.Column(db.String(255), nullable=False)
    slug_name = db.Column(db.String(255), nullable=True)
    
    #constructor
    # def __init__(self, parent_id=None, email=None, password=None):
    #     self.name = name
    #     self.email = email
    #     self.authenticated = True
    
    def getAll():
        return Category.query.all()
    
    def getById(id):
        return Category.query.get(id)