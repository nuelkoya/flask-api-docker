Flash API Docker
-----------------------------------------------------------------------------------------
A simple Flask API with PostgreSQL, containerized with Docker. This project demonstrates:
- Running multiple Flask containers with Docker Compose.
- Connecting Flask to a PostgreSQL database.
- Running tests in GitHub Actions.

Project Structure
-----------------------------------------------------------------------------------------
python_api_docker/
- ├── app.py                  # Flask app
- ├── database/               # DB connection, queries, setup
- ├── static/                 # CSS
- ├── templates/              # HTML templates
- ├── tests/                  # Pytest tests
- ├── Dockerfile              # Dockerfile for Flask app
- ├── compose.yaml     # Docker Compose setup
- ├── requirements.txt        # Python dependencies
- └── .github/workflows/
-     └── app_test.yml        # GitHub Actions workflow

Environment Variables
-----------------------------------------------------------------------------------------
Create a .env file (not committed to GitHub) with the following:
- POSTGRES_USER=your_postgres_user
- POSTGRES_PASSWORD=your_postgres_password
- POSTGRES_DB=your_database_name

These are used in:
- Docker Compose
- Flask DATABASE_URL

In GitHub Actions, these are provided as secrets:
DOCKER_POSTGRES_USER, DOCKER_POSTGRES_PASSWORD, DOCKER_POSTGRES_DB.


Running Locally with Docker Compose
-----------------------------------------------------------------------------------------
- Build and start containers:

- docker compose build
- docker compose up

- Access your APIs:
http://localhost:5100/ → flask-app-1
http://localhost:5200/ → flask-app-2

API Endpoints:
- / → Homepage
- /db → View all rows in test_data
- /submit_data → POST form submission to add data

Stop containers:
- docker compose down



Running Tests
-----------------------------------------------------------------------------------------
Locally (inside Python environment):

PYTHONPATH=. pytest


GitHub Actions automatically runs:
- Unit tests (pytest)
- Docker containers and endpoint checks


Notes
-----------------------------------------------------------------------------------------
Flask runs on port 5501 internally, mapped to different host ports in Compose.

PostgreSQL data is persisted in the db-data Docker volume.

.env is not committed to GitHub for security.

Make sure your DATABASE_URL points to the correct database container when running locally.