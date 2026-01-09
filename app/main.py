from fastapi import FastAPI
from app.database import engine, Base
from app.models.job import Job
from app.routes.tasks import router as task_router

# ✅ Correct table creation
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Distributed Task Scheduler")
app.include_router(task_router)
