from fastapi import APIRouter

from app.todos._todos_router import todo_router

main_router = APIRouter(prefix="/api")

main_router.include_router(todo_router, tags=["todos"])

