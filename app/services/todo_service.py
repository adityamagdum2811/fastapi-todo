from sqlalchemy.orm import Session
from typing import Optional, List
from app.database.models import Todo, TodoStatus, User
from app.schemas.todo_schema import TodoCreate, TodoUpdate

def create_todo(db: Session, owner: User, todo_in: TodoCreate) -> Todo:
    todo = Todo(
        title=todo_in.title,
        description=todo_in.description,
        user_id=owner.id,
        status=TodoStatus.pending
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def list_todos(db: Session, user: User, status: Optional[TodoStatus] = None, limit: int = 20, offset: int = 0) -> List[Todo]:
    q = db.query(Todo).filter(Todo.user_id == user.id)
    if status is not None:
        q = q.filter(Todo.status == status)
    return q.order_by(Todo.created_at.desc()).offset(offset).limit(limit).all()

def get_todo_by_id(db: Session, todo_id: int) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.id == todo_id).first()

def update_todo(db: Session, todo: Todo, todo_in: TodoUpdate) -> Todo:
    if todo_in.title is not None:
        todo.title = todo_in.title
    if todo_in.description is not None:
        todo.description = todo_in.description
    if todo_in.status is not None:
        todo.status = todo_in.status
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo: Todo) -> None:
    db.delete(todo)
    db.commit()
