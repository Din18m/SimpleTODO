from typing import Optional
from sqlalchemy.orm import Session
from database.models import Todo
from schemas import TodoUpdate


def update_todo(db: Session, todo_id: int, payload: TodoUpdate) -> Optional[Todo]:
    todo = db.get(Todo, todo_id)
    if not todo:
        return None

    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(todo, k, v)

    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
