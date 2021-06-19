from re import A
from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    db = sqlite3.connect("bdays.db")
    cur = db.cursor()
    rows = cur.execute("SELECT * FROM birthdays ORDER BY id")
    return render_template("index.html", rows=rows)

@app.route("/added", methods=["POST"])
def added():
    with sqlite3.connect("bdays.db") as db:
        cur = db.cursor()
        name = request.form.get("name")
        date = request.form.get("month") + "/" + request.form.get("day")
        sql = '''INSERT INTO birthdays(name, date) VALUES (?, ?)'''
        cur.execute(sql,(name, date))
        db.commit()
    return redirect("/")