from app import app
from flask import render_template, request, redirect, session
import games

@app.route("/")
def index():
    return render_template("index.html", games=games.get_all_games())

@app.route("/add_game", methods=["get", "post"])
def add_game():
    if request.method == "GET":
        return render_template("add_game.html")
    
    if request.method == "POST":
        title = request.form["title"]
        games.add_game(title)
    
        return redirect("/")

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username

        return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
