# Superheroes API

## Description

Superheroes API is a Flask-based RESTful API for managing superheroes and their superpowers.  
It allows users to view heroes, powers, assign powers to heroes, and test email functionality using Flask-Mail.  

---

## Author

**Joshua Biboko**

## Features

- Heroes
- List all heroes — `GET /heroes`
- Get a hero (with powers) — `GET /heroes/<id>`
- Powers
- List all powers — `GET /powers`
- Get a power — `GET /powers/<id>`
- Update a power's description — `PATCH /powers/<id>`
- Hero Powers
- Assign a power to a hero — `POST /hero_powers`
- Email testing
- Send a test email — `GET /test-email` (emails are suppressed in development)

## Technologies

- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Mail
- SQLAlchemy-Serializer
- SQLite

## Quickstart (Linux / macOS)

1. Clone the repository and create a virtual environment

```bash
git clone <your-repo-url>
cd superheroes-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

1. Set Flask environment variables

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

1. Prepare the database (if migrations not initialized)

```bash
flask db init   # only if migrations folder is missing
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py
```

1. Run the app

```bash
flask run --port 5555
# Visit: http://localhost:5555
```

Windows notes: use `venv\\Scripts\\activate` to activate the virtualenv and `set`/`setx` to set environment variables in PowerShell or CMD.

## API Endpoints

- `GET /heroes` — list all heroes
- `GET /heroes/<id>` — get a hero by ID (includes powers)
- `GET /powers` — list all powers
- `GET /powers/<id>` — get a power by ID
- `PATCH /powers/<id>` — update a power's description
- `POST /hero_powers` — assign a power to a hero
- `GET /test-email` — trigger test email (suppressed in development)

## Notes

- Flask-Mail uses `MAIL_SUPPRESS_SEND = True` in development so external emails are not sent.
- The project uses SQLite (`app.db`) and migrations are handled with Flask-Migrate.
