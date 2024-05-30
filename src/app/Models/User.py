from ...config.database import db, BaseModel
from flask_login import UserMixin

class User(UserMixin, BaseModel):
    __tablename__ = 'users'
    
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.CHAR(16), nullable=False)
    email_verified_at = db.Column(db.DateTime(16), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    remember_token = db.Column(db.String(255), nullable=True)
    