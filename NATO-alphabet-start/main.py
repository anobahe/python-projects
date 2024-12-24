import sys, pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# student_data_frame = pandas.DataFrame(student_dict)
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic_code():
    word = input("Enter a word: ").upper()
    if word == "EXIT":
        sys.exit()
    try:
        nato_word_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet allowed.")
        phonetic_code()
    else:
        print(nato_word_list)
        phonetic_code()


phonetic_code()
