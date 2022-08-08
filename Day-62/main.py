from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv




app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is the secret key of my coffee and wifi projects'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe_name = StringField("Cafe name", validators=[DataRequired()])
    cafe_location = StringField("Cafe_location", validators=[DataRequired(), URL()])
    opening_time = StringField("Opening Time", validators=[DataRequired()])
    closing_time = StringField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[DataRequired()])
    wifi_strength = SelectField('Wifi Strength Rating', choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                                validators=[DataRequired()])
    power_socket_availability = SelectField("power Socket Availability",
                                            choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                                            validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode='a',encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe_name.data},"
                           f"{form.cafe_location.data},"
                           f"{form.opening_time.data},"
                           f"{form.closing_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_strength.data},"
                           f"{form.power_socket_availability.data}")
        return redirect(url_for('cafes'))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file,delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes = list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
