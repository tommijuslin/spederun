from app import app
from flask import render_template, request, redirect, session, url_for
import users
import games
import runs
import platforms
import games_platforms

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
        user_id = request.form["user_id"]
        platform_id = request.form["selected_platform"]
        runs.add_run(id, time, platform_id, user_id)

        if not games_platforms.get_platform(platform_id):
            games_platforms.add_platform(id, platform_id)

        return redirect(url_for("game", id=id))
    
    return render_template("submit_run.html", game=games.get_game(id),
                                              platforms=platforms.get_all_platforms())

@app.route("/game/<int:id>")
def game(id):
    return render_template("game.html", game=games.get_game(id),
                                        runs=runs.get_runs(id),
                                        platforms=games_platforms.get_all_platforms(id))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Wrong username or password")
    
    return render_template("login.html")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords don't match")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration failed")
    
    return render_template("register.html")
    

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return redirect("/")
