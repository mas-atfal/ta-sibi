from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    name: str | None
    email: str
    phone: str


class User(UserCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(UserCreate):
    pass
