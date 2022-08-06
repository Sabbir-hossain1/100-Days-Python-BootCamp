from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

# For email validation pip install wtforms[email]

class LoginForm(FlaskForm):
    email = StringField("Email", [DataRequired(), validators.length(min=6, max=120), validators.Email()])
    password = PasswordField('Password', [DataRequired(), validators.length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "This is my secret key string"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
