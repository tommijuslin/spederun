from app import app
from flask import render_template, request, redirect, session, jsonify, make_response
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
        req = request.get_json()

        if users.login(req["username"], req["password"]):
            return make_response(jsonify({"redirect": "/"}))
        else:
            return make_response(jsonify({"message": "Wrong username or password."}))
    
    return render_template("login.html")


@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "POST":
        req = request.get_json()

        username = req["username"]
        password1 = req["password1"]
        password2 = req["password2"]

        message = None

        if len(username) < 1 or len(username) > 20:
            message = "Username must be 1-20 characters long."
        elif users.get_username(username):
            message="User with that name already exists."
        elif len(password1) < 8:
            message="Password must be at least 8 characters long."
        elif password1 != password2:
            message="Passwords don't match."

        if message:
            return make_response(jsonify({"message": message}))

        if users.register(username, password1):
            return make_response(jsonify({"redirect": "/"}))
            
    return render_template("register.html")

  
@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    del session["user_role"]
    return redirect("/")
