# UFC Fight Management Django App

A Django web application for managing UFC-style fight data, including fighters, events, fights, results, and weight classes.

## Highlights

- Relational Django models for fighters, events, fights, results, and divisions
- Server-rendered templates for browsing and editing records
- Forms and fixture data for fast local setup
- Basic static styling for a clean database-backed web interface

## Tech Stack

- Python
- Django
- HTML/CSS

## Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata ufc_app/fixtures/initial_data.json
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

