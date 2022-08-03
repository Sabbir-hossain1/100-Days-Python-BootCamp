from flask import Flask, request, render_template
import requests
import smtplib

posts = requests.get("https://api.npoint.io/dc686c6a0d2e5f24ed1c").json()
my_email = "higherstudyadmission@gmail.com"
my_password = "wahwogxwxcpkjvlq"

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact", methods=["GET", "POST"])
def received_data():
    if request.method == "POST":
        data = request.form
        send_mail(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg=True)
    return render_template("contact.html", msg=False)


def send_mail(name, email, phone, message):
    email_message = f"Subject: new Message from contact\n\n {name}\n {email}\n{phone}\n {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="sabbir.cse.duet@gmail.com",msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)
