from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel

class TaskCreate(BaseModel):
    name: str
    task_type: str            # 👈 REQUIRED
    payload: Optional[Dict[str, Any]] = None
    run_at: Optional[datetime] = None


class TaskResponse(BaseModel):
    id: int
    name: str
    status: str
    payload: Optional[Dict]
    run_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
