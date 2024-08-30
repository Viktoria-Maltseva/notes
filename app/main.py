from fastapi import FastAPI, Depends, HTTPException, responses
from sqlalchemy.orm import Session
from app import database, auth, speller, crud
from app.schemas import *


app = FastAPI()


database.create_tables_if_not_exists(database.engine)


@app.post("/register")
async def register(form: RegisterForm, db: Session = Depends(database.get_db)) -> dict:
    # Проверка, существует ли уже пользователь с таким именем или email
    existing_user = crud.get_user_by_username_or_email(db, form.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует")
    
    # Хэширование пароля
    hashed_password = auth.hash_password(form.password)
    
    # Создание нового пользователя
    crud.create_user(db, user=form.username, hashed_password=hashed_password)
    return {"message": "Пользователь успешно зарегистрирован"}


@app.post("/login")
async def login(form: LoginForm, db: Session=Depends(database.get_db)) -> dict:
    user = auth.authenticate_user(db, form.username, form.password)
    if not user:
        raise HTTPException(status_code=400, detail="Неправильный пароль или логин")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/notes/")
async def create_note(note: NoteCreate, db: Session=Depends(database.get_db), cur_user: User=Depends(auth.get_current_user)) -> dict:
    spelling_errors = speller.check_spelling(note.body)
    if spelling_errors:
        raise HTTPException(status_code=400, detail=f"Орфографические ошибки: {', '.join(spelling_errors)}")
    return crud.create_note(db=db, note=note, user_id=cur_user.id)


@app.get("/notes/")
async def read_notes(db: Session = Depends(database.get_db), current_user: User = Depends(auth.get_current_user)) -> responses.JSONResponse:
    notes = crud.get_notes(db, user_id=current_user.id)
    # Преобразуем кортежи в словари
    notes_dict = [{"title": title, "body": body} for title, body in notes]
    return responses.JSONResponse(content={"notes": notes_dict})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")