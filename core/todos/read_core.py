from typing import Sequence, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import Todo


def list_todos(db: Session, skip: int = 0, limit: int = 50) -> Sequence[Todo]:
    stmt = select(Todo).offset(skip).limit(limit)
    return db.execute(stmt).scalars().all()


def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    return db.get(Todo, todo_id)
