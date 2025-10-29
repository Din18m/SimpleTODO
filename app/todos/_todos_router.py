from fastapi import APIRouter

from app.todos.create import create
from app.todos.read import read
from app.todos.update import update
from app.todos.delete import delete

todo_router = APIRouter()

todo_router.include_router(create)
todo_router.include_router(read)
todo_router.include_router(update)
todo_router.include_router(delete)
