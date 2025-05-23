from flask import Flask, render_template, url_for
import requests
app = Flask("__main__", static_folder='static')

response = requests.get("https://api.npoint.io/890fc195c58eec63cca3").json


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
