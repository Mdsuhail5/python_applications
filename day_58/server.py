from flask import Flask, render_template
import requests


params = {
    "name": "add",
}
app = Flask("__main__")


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    agify_url = f"https://api.agify.io?name={name}"
    agify_response = requests.get(agify_url)
    agify_data = agify_response.json()
    age = agify_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/038e5ba057ec916a1ef3"
    respones = requests.get(blog_url)
    all_posts = respones.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

# for dynamic rendering visit jinja website
# templating in jinja we use {% %} to write the python code for,if and all
# url bulding
