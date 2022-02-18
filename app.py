from os import getenv
from flask import Flask

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes.main
import routes.users
import routes.games
import routes.runs
import routes.categories
