from .connection import get_connection

def create_tables():
    """Create tables if they don’t exist."""
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS test_data (
                        id SERIAL PRIMARY KEY,
                        value TEXT
                    );
                """)
        print("✅ Tables created successfully")
    except Exception as e:
        print(f"❌ Table creation failed: {e}")
