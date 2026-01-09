from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes.tasks import router as task_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Distributed Task Scheduler")

app.include_router(task_router)
