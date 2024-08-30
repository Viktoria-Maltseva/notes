from pydantic import BaseModel


class LoginForm(BaseModel):
    username: str
    password: str


class NoteBase(BaseModel):
    title: str
    body: str


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class NoteSummary(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class RegisterForm(BaseModel):
    username: str
    password: str