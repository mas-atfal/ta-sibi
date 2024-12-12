from ...config.database import db, BaseModel

class Word(BaseModel):
    __tablename__ = 'words'

    #table columns
    alphabet_id = db.Column(db.BigInteger, db.ForeignKey('alphabets.id') , nullable=False)
    name = db.Column(db.String(255), nullable=False)
    slug_name = db.Column(db.String(255), nullable=False)
    video_link = db.Column(db.Text(), nullable=False)
    
    alphabet = db.relationship('Alphabet', backref='words', lazy=True, uselist=False)
    
    
    def getNameAlphabet(self):
        return self.alphabet.name
    
    #constructor
    # def __init__(self, parent_id=None, email=None, password=None):
    #     self.name = name
    #     self.email = email
    #     self.authenticated = True
    
    def jsonResponse(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug_name': self.slug_name,
            'video_link': self.video_link
        }