# AI Resolution Engine

Core AI orchestration service for Helply's autonomous support agent. Handles ticket classification, context retrieval via RAG, action execution (refunds, account updates), and smart escalation.

**Stack:** Python 3.11, Django 4.2, Celery, Redis, PostgreSQL, OpenAI GPT-4

**Run locally:** `docker-compose up` then `python manage.py runserver`