# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
import random
from datetime import datetime as dt
import pandas as pd
import smtplib

SENDER_EMAIL = "skillpickethioinfo@gmail.com"
SENDER_PASSWD = "***********"

today = dt.now()
today_tuple = (today.month, today.day)
data = pd.read_csv("birthdays.csv")
new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in new_dict:
    birthday_boy = new_dict[today_tuple]
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as letter_file:
        content = letter_file.read()
        message =  content.replace("[Name]", birthday_boy["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWD)
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=birthday_boy["email"],
                            msg=f"Subject:Happy Birthday!\n\n{message}")
