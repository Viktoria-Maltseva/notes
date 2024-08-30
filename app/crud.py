from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext
from app.models import User
from typing import Optional, Dict, List


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_username_or_email(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def get_user(db: Session, username: str) -> Optional[User]:
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate, hashed_password) -> User:
    db_user = models.User(username=user, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_note(db: Session, note: schemas.NoteCreate, user_id: int) -> Dict[str, str]:
    db_note = models.Note(**note.model_dump(), owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return {db_note.title: db_note.body}


def get_notes(db: Session, user_id: int) -> List[Dict[str, str]]:
    notes = db.query(models.Note.title, models.Note.body).filter(models.Note.owner_id == user_id).all()
    return notes