import pandas

content = pandas.read_csv("birthdays.csv")

# for i, row in content.iterrows():
#     print(0["year"])

with open("letter_templates/letter_1.txt", "r") as file:
    text = file.read()
    new_text = text.replace('[NAME]', 'EBEN')
    print(new_text)