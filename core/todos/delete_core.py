from sqlalchemy.orm import Session

from database.models import Todo


def delete_todo(db: Session, todo_id: int) -> bool:
    todo = db.get(Todo, todo_id)
    if not todo:
        return False
    db.delete(todo)
    db.commit()
    return True
