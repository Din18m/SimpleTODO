from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database.models import get_db
from schemas import TodoUpdate, TodoOut
from core.todos.update_core import update_todo

update = APIRouter()


@update.patch("/todos/{todo_id}", response_model=TodoOut)
def http_update_todo(todo_id: int, payload: TodoUpdate, db: Session = Depends(get_db)):
    todo = update_todo(db, todo_id, payload)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
