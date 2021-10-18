##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import smtplib
import random
import os

# Constants
MY_EMAIL = os.environ.get("SECRET_EMAIL")
MY_PASSWORD = os.environ.get("SECRET_PASSWORD")

# Find today's date
now = dt.datetime.now()
day_of_month = now.day
month = now.month

# Create birthday dictionary to loop through
with open("birthdays.csv") as birth_data:
    birthdays = pandas.read_csv(birth_data)
    birthdays_dict = birthdays.to_dict(orient="records")

# Check if it is someone's birthday today
for person in birthdays_dict:
    if person["month"] == month and person["day"] == day_of_month:
        number = random.randint(1, 3)

        # Open and random letter and replace with the correct name
        with open(f"letter_templates/letter_{number}.txt") as letter:
            final_letter = letter.read()
            final_letter = final_letter.replace("[NAME]", person["name"])

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"], msg=f"Subject:Happy Birthday!\n\n"
                                                                                  f"{final_letter}")

