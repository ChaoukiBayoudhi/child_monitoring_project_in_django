# Child monitoring project in Django

A Django project with 5 models and a REST API (Django REST Framework).

## Tech stack

- Python 3
- Django
- Django REST Framework
- Database: PostgreSQL

## Project structure

- `child_monitoring_project/`: project settings and root URLs
- `child_app/`: Django app
- Tests: `child_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Person` | `child_app` | firstName, lastName, birthDate, photo |
| `Parent` | `child_app` | — |
| `Child` | `child_app` | studyLevel, parent |
| `Place` | `child_app` | longitude, lattitude, children |
| `ChildPlace` | `child_app` | child, place, date, time |

## URL routes

Declared in `urls.py`:

- `/blog/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install django djangorestframework psycopg2-binary
python manage.py migrate
python manage.py runserver
```

There is no `requirements.txt`; the packages above are the ones the settings and imports refer to.

`settings.py` is configured for PostgreSQL: create the database and use your own credentials before running `migrate`.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
