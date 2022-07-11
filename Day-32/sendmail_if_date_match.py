import random
import datetime as dt
import smtplib

my_email = "higherstudyadmission@gmail.com"
password = "wahwogxwxcpkjvlq"

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 0:
    with open("./quotes.txt") as datafile:
        quote = datafile.readlines()
        random_quote = random.choice(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="sabbir.cse.duet@gmail.com",
                            msg=f"Subject: Quote \n\n {random_quote}")

