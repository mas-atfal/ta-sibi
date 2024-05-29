from ...config.database import db, BaseModel
from .Category import Category

class Article(BaseModel):
    __tablename__ = 'articles'

    user_id = db.Column(db.BigInteger, nullable=False)
    category_id = db.Column(db.BigInteger, db.ForeignKey('categories.id') , nullable=False)
    title = db.Column(db.String(255), nullable=False)
    slug_title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    status = db.Column(db.Enum('published', 'draft'), nullable=False)
    image = db.Column(db.Text(), nullable=False)
    
    category = db.relationship('Category', backref='articles', lazy=True, uselist=False)
    
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