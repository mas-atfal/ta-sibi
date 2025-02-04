from ...config.database import db, BaseModel

class Category(BaseModel):
    __tablename__ = 'categories'

    parent_id = db.Column(db.BigInteger, nullable=True)
    name = db.Column(db.String(255), nullable=False)
    slug_name = db.Column(db.String(255), nullable=False)
    
    #constructor
    # def __init__(self, parent_id=None, email=None, password=None):
    #     self.name = name
    #     self.email = email
    #     self.authenticated = True
    
    def jsonResponse(self):
        return {
            'id': self.id,
            'name': self.name
        }