from flask import (
    Flask,
    request
)
from random import randint
import template_engine
import json
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    first, second = randint(1, 10), randint(1, 10)
    return template_engine.render("index.json", first=first, second=second)


@app.route("/gmail_homepage", methods=['POST', 'GET'])
def gmail_homepage():
    return template_engine.render("gmail_homepage.json")


@app.route("/gmail_compose", methods=['POST'])
def gmail_compose():
    print(request.headers)
    print(request.form.to_dict())


@app.route("/gmail_opened", methods=['POST'])
def gmail_opened():
    data = json.loads(request.data)
    print(data)
    return template_engine.render("index.json")


if __name__ == "__main__":
    app.run()
