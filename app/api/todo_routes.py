from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from app.api.deps import get_db_dep, get_current_user
from app.schemas.todo_schema import TodoCreate, TodoOut, TodoUpdate, TodoStatus
from app.services.todo_service import create_todo, list_todos, get_todo_by_id, update_todo, delete_todo

router = APIRouter()

@router.post("/", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def create(todo_in: TodoCreate, db: Session = Depends(get_db_dep), current_user=Depends(get_current_user)):
    todo = create_todo(db, owner=current_user, todo_in=todo_in)
    return todo

@router.get("/", response_model=List[TodoOut])
def read_todos(
    db: Session = Depends(get_db_dep),
    current_user=Depends(get_current_user),
    status: Optional[TodoStatus] = Query(None),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    return list_todos(db, user=current_user, status=status, limit=limit, offset=offset)

@router.get("/{todo_id}", response_model=TodoOut)
def read_todo(todo_id: int, db: Session = Depends(get_db_dep), current_user=Depends(get_current_user)):
    todo = get_todo_by_id(db, todo_id)
    if not todo or todo.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoOut)
def put_todo(todo_id: int, todo_in: TodoUpdate, db: Session = Depends(get_db_dep), current_user=Depends(get_current_user)):
    todo = get_todo_by_id(db, todo_id)
    if not todo or todo.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    updated = update_todo(db, todo, todo_in)
    return updated

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_todo(todo_id: int, db: Session = Depends(get_db_dep), current_user=Depends(get_current_user)):
    todo = get_todo_by_id(db, todo_id)
    if not todo or todo.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    delete_todo(db, todo)
    return None
