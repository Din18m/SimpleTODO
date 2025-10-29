from typing import List
from fastapi import Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi import APIRouter

from database.models import get_db
from schemas import TodoOut
from core.todos.read_core import list_todos, get_todo

read = APIRouter()


@read.get("/", response_model=List[TodoOut])
def http_list_todos(
        skip: int = Query(0, ge=0),
        limit: int = Query(50, ge=1, le=200),
        db: Session = Depends(get_db),
):
    return list_todos(db, skip=skip, limit=limit)


@read.get("/{todo_id}", response_model=TodoOut)
def http_get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
