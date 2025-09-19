import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    """Return a new Postgres connection."""
    return psycopg2.connect(DATABASE_URL)