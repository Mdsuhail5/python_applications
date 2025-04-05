from flask import Flask

app = Flask("__main__")


@app.route("/")
def home():
    print "Hello world"


if __name__ == "__main__":
    app.run()
