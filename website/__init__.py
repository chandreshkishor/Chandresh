from flask import Flask

app = Flask(__name__)

from website.main.routes import main

app.register_blueprint(main)
