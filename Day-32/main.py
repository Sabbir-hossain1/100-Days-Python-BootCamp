import random
import smtplib

import pandas as pd
import datetime as dt

my_email = "higherstudyadmission@gmail.com"
password = "wahwogxwxcpkjvlq"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birth_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birth_dict:
    birth_day_person = birth_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as datafile:
        get_name = datafile.read()
        new_letter = get_name.replace("[NAME]", birth_day_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birth_day_person["email"],
                            msg=f"Subject: Happy Birthday! \n\n{new_letter}")
