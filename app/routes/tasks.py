print(">>> tasks.py loading")

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models import Task
from app.schemas import TaskCreate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    status = "SCHEDULED" if task.run_at else "PENDING"

    new_task = Task(
        name=task.name,
        payload=task.payload,
        run_at=task.run_at,
        status=status
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session

# from app.database import get_db
# from app.models import Task
# from app.schemas import TaskCreate, TaskResponse

# router = APIRouter(
#     prefix="/tasks",
#     tags=["Tasks"]
# )

# @router.post("/",response_model=TaskResponse)
# def create_task(task: TaskCreate, db: Session = Depends(get_db)):
#     status = "SCHEDULED" if task.scheduled_at else "PENDING"

#     db_task = Task(
#         name = task.name,
#         payload = task.payload,
#         scheduled_at = task.scheduled_at,
#         status = status
#     )   

#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)

#     return db_task

# @router.get("/{task_id}",response_model=TaskResponse)
# def get_task(task_id: str, db: Session = Depends(get_db)):
#     task = db.query(Task).filter(Task.id == task_id).first()

#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
    
#     return task