from sqlalchemy import Column, Integer, String, DateTime, JSON, func
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(36), nullable=False)
    status = Column(String(50), nullable=False, default="PENDING")

    payload = Column(JSON, nullable=True)

    run_at = Column(DateTime, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )