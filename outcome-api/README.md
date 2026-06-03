# Outcome API

Tracks AI outcomes (resolutions, drafts, escalations), validates quality via CSAT and accuracy checks, enforces the 65% guarantee SLA, and generates billing events for Stripe.

**Stack:** Python 3.11, Django 4.2, PostgreSQL, Redis, Stripe API

**Run locally:** `docker-compose up` then `python manage.py runserver 8001`