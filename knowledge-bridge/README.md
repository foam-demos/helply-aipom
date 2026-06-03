# Knowledge Bridge

Analyzes resolved and escalated tickets to identify knowledge gaps, auto-drafts missing KB articles using GPT-4, and syncs content updates from help center APIs.

**Stack:** Python 3.11, Django 4.2, Celery, Pinecone (vector DB), OpenAI GPT-4

**Run locally:** `docker-compose up` then `celery -A tasks worker --loglevel=info`