from ...config.database import db
from .BaseModel import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    
    title = db.Column(db.String(255), nullable=False)
    slug_title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    # password: Mapped[str] = mapped_column(nullable=False)
    
    #constructor
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        # self.password = password
        self.authenticated = True