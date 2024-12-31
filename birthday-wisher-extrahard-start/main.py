##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib, random, pandas

my_email = "adjeimanuspendilove812@gmail.com"
password = "pyiwybrdnkkiybes"

content = pandas.read_csv("birthdays.csv")

# 1. Update the birthdays.csv
now = dt.datetime.now()

for index, row in content.iterrows():
    if now.month == row["month"] and now.day == row["day"]:
        letter = random.choice(["letter_templates/letter_1.txt", "letter_templates/letter_2.txt",
                                "letter_templates/letter_3.txt"])
        with open(letter, "r") as file:
            text = file.read()
            new_text = text.replace('[NAME]', row["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday {row['name']}!\n\n{new_text}")

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




