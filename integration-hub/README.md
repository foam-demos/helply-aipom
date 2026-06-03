# Integration Hub

Manages bidirectional sync with 20+ third-party platforms (help desks, CRMs, billing). Handles webhook ingestion, OAuth flows, rate limiting, and retry logic.

**Stack:** Python 3.11, Django 4.2, Celery, Redis, PostgreSQL

**Run locally:** `make dev` or `docker-compose up && python manage.py migrate`