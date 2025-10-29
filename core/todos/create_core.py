from sqlalchemy.orm import Session
from database.models import Todo
from schemas import TodoCreate


def create_todo(db: Session, payload: TodoCreate) -> Todo:
    todo = Todo(**payload.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
