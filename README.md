**Distributed Task Scheduler (Backend-Only)**

A backend-first distributed task scheduling system built with FastAPI, relational persistence, Redis-based queuing, and worker execution — inspired by real-world orchestration systems like Airflow, Celery, and Temporal.

This project focuses on correctness, reliability, and system design, intentionally excluding a frontend UI.

Project Goals

-- Build a persistent, reliable task scheduler

-- Separate concerns between:

    --- API

    --- Scheduling

    --- Execution

    --- Support delayed execution, retries, and failure handling

    --- Demonstrate production-grade backend architecture



🧩 Component Responsibilities
1️⃣ FastAPI (API Layer)

Exposes HTTP APIs to:

--> Create tasks

--> Query task status

--> Stateless

--> Does not execute tasks

--> Acts as the external contract

2️⃣ Database (Source of Truth)

--> Stores all task metadata and state

--> Guarantees durability

--> Enables recovery after crashes

--> All state transitions are persisted

3️⃣ Scheduler Engine

--> Runs as a separate background process

Periodically:

--> Polls DB for SCHEDULED tasks

--> Checks run_at <= current_time

--> Pushes eligible tasks to Redis

--> Responsible for when tasks should run

4️⃣ Redis (Queue / Transport Layer)

--> Acts as a fast message broker

--> Decouples scheduler and workers

--> Enables horizontal scaling

--> Provides at-least-once delivery semantics

5️⃣ Worker System

--> One or more independent worker processes

--> Consumes task IDs from Redis

--> Executes task logic

--> Updates task state in DB

--> Handles retries and failures


🚀 API Overview
Create Task
POST /tasks/

{
  "name": "send_email",
  "payload": {
    "to": "user@example.com"
  },
  "run_at": "2026-01-09T10:00:00"
}

Get Task Status
GET /tasks/{task_id}

Design Principles:

-- Backend-first by design

-- Database as the single source of truth

-- Clear separation of concerns

-- Loose coupling via Redis

-- Scalable by adding workers

-- Recoverable after failures


This mirrors how such systems are built and operated in production environments.

🛣️ Development Roadmap

Day 01 – Project setup & Redis validation

Day 02 – Task model & APIs

Day 03 – Scheduler engine (DB → Redis)

Day 04 – Worker execution system

Day 05 – Reliability (retries, idempotency)

Day 06 – Scaling & concurrency

Day 07 – Observability & polish
