from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from database.models import get_db
from schemas import TodoCreate, TodoOut
from core.todos.create_core import create_todo

create = APIRouter()


@create.post("/", status_code=201, response_model=TodoOut)
def http_create_todo(payload: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, payload)
