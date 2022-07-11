import datetime as dt

# accessing default date and time module
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
print(year, month, day)

# Creating own date and time module
date_of_birth = dt.datetime(year=1994, month=12, day=23)
print(date_of_birth)