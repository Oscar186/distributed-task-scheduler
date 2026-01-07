from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    name: str
    payload: Optional[dict] = None
    scheduled_at: Optional[datetime] = None


class TaskResponse(BaseModel):
    id: str
    status: str
    scheduled_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
