import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://trqtddsfwsydqm:d981464912f8a12a97e77298661800f75f904a02b66544aeca2ec587cb614722@ec2-54-197-48-79.compute-1.amazonaws.com:5432/d7ntbcs9nbv9tr'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import views