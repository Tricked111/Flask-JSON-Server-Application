from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Movies,database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JSON_SORT_KEYS'] = False
database.init_app(app)



@app.route('/')
def index():
    """ Index route """
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True)