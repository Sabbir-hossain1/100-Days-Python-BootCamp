import smtplib

my_email = "higherstudyadmission@gmail.com"
password = "wahwogxwxcpkjvlq"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="sabbir.cse.duet@gmail.com",
                        msg="Subject: Testing Mail\n\n this is the mail body")
