from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.orm import declarative_base
import datetime
import uuid

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    payload = Column(JSON, nullable=True)
    status = Column(String(50), nullable=False)
    scheduled_at = Column(DateTime, nullable=True)  # <-- MAKE THIS NULLABLE
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
