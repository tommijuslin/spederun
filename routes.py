from app import app
from flask import render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import games
import runs

@app.route("/")
def index():
    return render_template("index.html", games=games.get_all_games())

@app.route("/add_game", methods=["get", "post"])
def add_game():
    if request.method == "POST":
        title = request.form["title"]
        games.add_game(title)
    
        return redirect("/")
    
    return render_template("add_game.html")

@app.route("/game/<int:id>/submit_run", methods=["get", "post"])
def submit_run(id):
    if request.method == "POST":
        time = request.form["time"]
        user = request.form["username"]
        runs.add_run(id, time)

        return redirect(url_for("game", id=id))
    
    return render_template("submit_run.html", game=games.get_game(id))

@app.route("/game/<int:id>")
def game(id):
    all=runs.get_runs_for(id)

    print(len(all))

    return render_template("game.html", game=games.get_game(id), runs=all)

@app.route("/login", methods=["get", "post"])
def login():        
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username

        return redirect("/")
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
