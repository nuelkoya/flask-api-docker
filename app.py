from flask import Flask, request, render_template
from database.setup import create_tables
from database.queries import add_text_to_db, get_all_rows
import os

app = Flask(__name__)

# Create tables when container starts
create_tables()

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/db")
def db_test():
    return get_all_rows()


@app.route("/submit_data", methods=['GET', 'POST'])
def submit_data():
    if request.method == 'POST':
        fav_food = request.form.get('fav_food')
        add_text_to_db(fav_food)
        return render_template('submit.html', fav_food=fav_food)
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5501)
