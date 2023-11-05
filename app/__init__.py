from flask import Flask
from flask_login import LoginManager
from flask import Flask, render_template
from app import routes

app = Flask(__name__)
login_manager = LoginManager(app)

@app.route('/')

def home():
    return "Hello world"

