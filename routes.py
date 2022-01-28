from app import app
from flask import render_template, request, redirect
import games

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_game", methods=["get", "post"])
def add_game():
    if request.method == "GET":
        return render_template("add_game.html")
    
    if request.method == "POST":
        title = request.form["title"]
        games.add_game(title)
    
        return redirect("/")
