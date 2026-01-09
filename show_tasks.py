# show_tasks.py
from app.database import SessionLocal
from app.models.job import Task

db = SessionLocal()
tasks = db.query(Task).all()
for t in tasks:
    print(f"Task: {t.id}, Name: {t.name}, Status: {t.status}, Scheduled At: {t.scheduled_at}")
