# UFC Fight Management Django App

A Django web application for managing UFC-style fight data, including fighters, events, fights, results, and weight classes.

## Project Goal

The goal of this project is to build a database-backed web application that stores and displays fight management data through Django models, views, forms, templates, and fixtures.

## Data Source

The project uses sample fixture data included in:

- `ufc_app/fixtures/initial_data.json`

The fixture includes example weight classes, fighters, events, fights, and fight results. The data is for demonstration and local development.

## Main Components

- Django models: `WeightClass`, `Fighter`, `Event`, `Fight`, `FightResult`
- Django admin integration
- Model forms for creating and editing records
- Server-rendered templates
- Fixture loading for fast setup

## Final Result

The final app can be run locally and used to browse, add, and manage UFC-style fight records. Since this is a web application rather than an ML project, the result is measured by functionality instead of model metrics.

## What I Learned

- How to design relational models in Django
- How to connect models, forms, views, templates, and URLs
- How to use fixtures to load starter data
- How to structure a small full-stack Django project

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
