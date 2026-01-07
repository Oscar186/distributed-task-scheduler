from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes.tasks import router as task_router

#Create the APP instance with this exact name
app = FastAPI(title="Distributed Task Scheduler",debug=True)

#create db tables
models.Base.metadata.create_all(bind = engine)

@app.get("/health")
def health_check():
    return {"status": "Good"}

app.include_router(task_router)