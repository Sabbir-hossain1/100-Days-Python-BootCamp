from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/guess/<name>")
def guess(name):
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    received_name = name.title()
    age_response = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender_response = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("guess.html", year=current_year, name=received_name, age=age_response,
                           gender=gender_response)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_blog = response.json()
    return render_template("blog.html", posts=all_blog)


if __name__ == "__main__":
    app.run(debug=True)
