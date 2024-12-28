# import smtplib
#
# my_email = "adjeimanuspendilove812@gmail.com"
# password = "pyiwybrdnkkiybes"
#
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.ehlo()
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="pythondeveloper12@yahoo.com",
#                         msg="Subject:Hello World!\n\nThis is the body of my email.")


# def tri_recursion(k):
#     if k > 0:
#         result = k+tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# print("\n\nRecursion Example Results")
# tri_recursion(10)


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1992, month=8, day=9, hour=8)
print(date_of_birth)
