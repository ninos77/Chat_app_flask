import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "some_secret"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/disciples.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", disciples=data)


@app.route("/about/<disciple_name>")
def about_disciple(disciple_name):
    disciple = {}

    with open("data/disciples.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == disciple_name:
                disciple = obj
    return render_template("disciples.html", disciple=disciple)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash(f'Thanks {request.form["name"]}, We have recived your message')
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
