from ...config.database import db, BaseModel
from flask_login import UserMixin
import os, jwt, base64
from time import time
from werkzeug.security import generate_password_hash

class User(UserMixin, BaseModel):
    __tablename__ = 'users'
    
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.CHAR(16), nullable=False)
    email_verified_at = db.Column(db.DateTime(16), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    remember_token = db.Column(db.String(255), nullable=True)
    reset_password_token = db.Column(db.String(255), nullable=True)
    
    def __init__(self, password, email = None):
        if password != '':
            self.password = generate_password_hash(password)
        if email:
            self.email = email
            
    def setPassword(self, password, commit=False):
        self.password = generate_password_hash(password)
        if commit:
            db.session.commit()
    
    def getResetToken(self, expires=3600):
        return jwt.encode({'reset_password_token': self.email, 'exp': time() + expires}, key=os.getenv("SECRET_KEY"), algorithm="HS256")
    
    @staticmethod
    def verifyResetToken(token):
        try:
            email = jwt.decode(token, key=os.getenv("SECRET_KEY"), algorithms=["HS256"])['reset_password_token']
            return User.query.filter_by(email=email).first()
        except Exception as e:
            return False
    
    @staticmethod
    def verifyEmail(email):
        return User.query.filter_by(email=email).first()