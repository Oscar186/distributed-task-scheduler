import time
import random

def execute_job(job):

    print(f"🚀 Executing Job {job.id} | {job.name}")

    time.sleep(1)

    if random.choice([True,False]):
        raise Exception("Simulation job failure")
    
    print(f"✅ Job {job.id} completed successfully")

