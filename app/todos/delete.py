from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database.models import get_db
from core.todos.delete_core import delete_todo

delete = APIRouter()


@delete.delete("/todos/{todo_id}", status_code=204)
def http_delete_todo(todo_id: int, db: Session = Depends(get_db)):
    ok = delete_todo(db, todo_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
