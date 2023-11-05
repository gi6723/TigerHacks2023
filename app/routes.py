from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
