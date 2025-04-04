from flask import Flask, render_template
import random
import datetime as dt
app = Flask("__main__")


@app.route("/")
def home():
    random_no = random.randint(1, 10)
    current_yr = dt.datetime.now().year
    return render_template("index.html", num=random_no, year=current_yr)


if __name__ == "__main__":
    app.run(debug=True)


# templates are used to store and help server render html pages
# static floder is used to store images and css and used to render on the website by changing the path in html
# render template is used to render the html and static pages to the browser
# jinja is a templating language
