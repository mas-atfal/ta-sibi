from sqlalchemy.orm import Mapped, mapped_column
from .BaseModel import CreatedUpdatedAtMixin

class User(CreatedUpdatedAtMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    # password: Mapped[str] = mapped_column(nullable=False)
    
    #constructor
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        # self.password = password
        self.authenticated = True