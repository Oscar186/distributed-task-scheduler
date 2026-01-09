from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.job import Job
from app.redis_client import redis_client
import time

REDIS_QUEUE = "job_queue"


def execute_job(job: Job):
    print(f"🚀 Executing job {job.id} - {job.name}")
    time.sleep(2)  # simulate work
    print(f"✅ Job {job.id} done")


def worker_loop():
    print("👷 Worker started")

    while True:
        _, job_id = redis_client.brpop(REDIS_QUEUE)

        db: Session = SessionLocal()
        try:
            job = db.query(Job).filter(Job.id == int(job_id)).first()
            if not job:
                continue

            job.status = "RUNNING"
            db.commit()

            execute_job(job)

            job.status = "SUCCESS"
            db.commit()

        except Exception as e:
            job.retry_count += 1
            job.status = "FAILED"
            db.commit()
            print(f"❌ Job {job.id} failed: {e}")

        finally:
            db.close()
