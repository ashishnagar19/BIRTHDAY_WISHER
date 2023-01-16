import smtplib
import random
import pandas as pd
from _datetime import datetime
today = (datetime.now().month, datetime.now().day)
data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="ash92199@gmail.com", password="hagikfnjqpofdwkb")
        connection.sendmail(from_addr="ash92199@gmail.com", to_addrs=birthday_person["email"], msg=f"Subject:Birthday wish\n\n{contents}")

