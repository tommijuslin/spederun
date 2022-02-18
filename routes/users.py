from app import app
from flask import render_template, request, redirect, session
from utils import format_time
import users
import runs


@app.route("/user/<int:id>")
def user(id):
    allow = False
    user = users.get_user(id)

    if "user_id" in session:
        if session["user_id"] == id or users.require_role(1):
            allow = True

    if user:
        return render_template(
            "user.html",
            user=users.get_user(id),
            runs=runs.get_runs_for_user(id),
            format_time=format_time,
            allow=allow
        )

    return render_template("error.html", message=f"No user with id { id } could be found.")


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("login.html", message="Wrong username or password.")
    
    return render_template("login.html")


@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template(
                "register.html", message="Username must be 1-20 characters long."
            )
        if users.get_username(username):
            return render_template(
                "register.html", message="User with that name already exists."
            )

        password1 = request.form["password1"]
        if len(password1) < 8:
            return render_template(
                "register.html",
                message="Password must be at least 8 characters long."
            )
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("register.html", message="Passwords don't match.")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("register.html", message="Registration failed.")
    
    return render_template("register.html")

  
@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    del session["user_role"]
    return redirect("/")
