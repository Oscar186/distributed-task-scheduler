from sqlalchemy import Column, Integer, String, DateTime, JSON, func
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(36), nullable=False)
    task_type = Column(String(100), nullable=False)
    payload = Column(JSON, nullable=True)
    status = Column(String(50), nullable=False, default="PENDING")
    run_at = Column(DateTime, nullable=True)
    retry_count = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

# class Job(Base):
#     __tablename__ = "jobs"

#     id = Column(Integer, primary_key=True, index=True)

#     name = Column(String(36), nullable=False)
#     task_type = Column(String(100), nullable = False)
#     payload = Column(JSON, nullable=True)
#     status = Column(String(50), nullable=False, default="PENDING")
#     run_at = Column(DateTime, nullable=True)
#     retry_count = Column(Integer, default=0)
#     created_at = Column(DateTime, server_default=func.now())
#     max_retries = Column(Integer, default = 3)
#     updated_at = Column(
#         DateTime,
#         server_default=func.now(),
#         onupdate=func.now()
#     )