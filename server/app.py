# server/app.py
#!/usr/bin/env python3
from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Earthquake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return jsonify({"message": "Flask SQLAlchemy Lab 1"}), 200

@app.route('/earthquakes')
def get_earthquakes():
    quakes = Earthquake.query.all()
    return jsonify([quake.to_dict() for quake in quakes]), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)

