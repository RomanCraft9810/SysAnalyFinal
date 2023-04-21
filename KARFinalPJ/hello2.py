from flask import Flask, redirect, url_for, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/Welcome')
def hello_world():
	return render_template("Welcome.htm")

@app.route('/Confirmation')
def success():
    return render_template("Confirmation.htm")

@app.route('/Reservations')
def list():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row

    cmd = "SELECT * FROM rooms"
    cur = conn.cursor()
    cur.execute(cmd)
    rows = cur.fetchall()
    conn.close()
    return render_template("Reservations.htm", rows = rows)

@app.route("/Roomslist")
def addrec():
	return render_template("Roomslist.htm")

if __name__ == "__main__":
	app.run()
