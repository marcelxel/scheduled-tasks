# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
my_email_1 = os.environ.get("MY_EMAIL")
password_1 = os.environ.get("MY_PASSWORD")

# 1. Update the birthdays.csv
df_birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month,data_row.day):data_row for (index, data_row) in df_birthdays.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv
today = (dt.datetime.now().month,dt.datetime.now().day)
if today in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as file:
        letter = file.read()
        name = birthdays_dict[today]["name"]
        letter = letter.replace("[NAME]",name)

    # 4. Send the letter generated in step 3 to that person's email address.
    email_2 = birthdays_dict[today]["email"]
    with smtplib.SMTP("smtp.gmail.com") as connexion:
        connexion.starttls()
        connexion.login(user=my_email_1,password=password_1)
        connexion.sendmail(from_addr=my_email_1,to_addrs=email_2,msg=f"Subject: Happy Birthday!\n\n{letter}")
