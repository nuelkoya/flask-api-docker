from flask import Flask, request, render_template
from .connection import get_connection

def add_text_to_db(text):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO test_data (value) VALUES (%s) RETURNING id;",
                    (text,)
                )
                new_id = cursor.fetchone()[0]
        return f"<p>Inserted '{text}' with id {new_id}</p>"
        
    except Exception as e:
        return f"<p>❌ Insert failed: {e}</p>"

def get_all_rows():
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM test_data;")
                rows = cursor.fetchall()
        #return "<br>".join([f"id={r[0]}, value={r[1]}" for r in rows])
        return render_template('db.html', rows=rows)
    except Exception as e:
        #return f"<p>❌ Read failed: {e}</p>"
        return render_template('db.html', rows=rows)
