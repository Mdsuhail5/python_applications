# import requests

# response = requests.get("https://www.google.com")
# print(response.status_code)

# Flask
# Minimal flask application
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
        '<p> This is a paragraph tag</p>'


@app.route("/username/<name>")
def greet(name):
    return f"I m {name}"


if __name__ == "__main__":
    app.run(debug=True)
