from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import random
import os

app = Flask(__name__, template_folder="template")
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-change-me")

@app.route("/")
def home():
    return render_template("index.html")