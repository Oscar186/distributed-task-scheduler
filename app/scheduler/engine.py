# app/scheduler/engine.py
import time
from datetime import datetime
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.job import Job
from app.scheduler.executor import execute_job
from app.redis_client import redis_client

POLL_INTERVAL = 5  # seconds
REDIS_QUEUE = "job_queue"

def scheduler_loop():
    print("🕒 Scheduler started...")

    while True:
        db: Session = SessionLocal()
        try:
            now = datetime.utcnow()

            jobs = (
                db.query(Job)
                .filter(Job.status == "PENDING")
                .filter(Job.run_at <= now)
                .all()
            )

            for job in jobs:

                redis_client.lpush(REDIS_QUEUE,job.id)

                job.status = "QUEUED"
                db.commit()

                print(f"📤 Job {job.id} pushed to Redis")
                # try:
                #     job.status = "RUNNING"
                #     db.commit()

                #     execute_job(job)

                #     job.status = "SUCCESS"
                #     db.commit()

                # except Exception as e:
                #     job.retry_count += 1
                #     if job.retry_count >= job.max_retries:
                #         job.status = "FAILED"
                #     else:
                #         job.status = "PENDING"

                #     db.commit()
                #     print(f"❌ Job {job.id} failed: {e}")

        finally:
            db.close()

        time.sleep(POLL_INTERVAL)
