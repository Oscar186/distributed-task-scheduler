from datetime import datetime
from typing import Optional, Dict
from pydantic import BaseModel

class TaskCreate(BaseModel):
    name: str
    payload: Optional[Dict] = None
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



# from pydantic import BaseModel, ConfigDict
# from typing import Optional
# from datetime import datetime

# class TaskCreate(BaseModel):
#     name: str
#     payload: Optional[dict] = None
#     scheduled_at: Optional[datetime] = None


# class TaskResponse(BaseModel):
#     id: str
#     status: str
#     scheduled_at: Optional[datetime]

#     model_config = ConfigDict(from_attributes=True)
