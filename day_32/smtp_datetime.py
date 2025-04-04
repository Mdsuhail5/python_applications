# using smtp protocol to send emails
import datetime as dt
import smtplib
my_email = ""
my_password = ""

with smtplib.SMTP("smtp.gmail.com")as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=""
        msg="Subject:    \n "
    )

# printing the date and time
now = dt.datetime.now()

print(now.month)
print(now.year)
print(now.weekday())
print(now.year)
print(type(now))

DOB = dt.datetime(year=2003, month=8, day=4, hour=4)
print(DOB)
