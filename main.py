import pandas

nato_phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")

data = {value.letter: value.code for (index, value) in nato_phonetic_data.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_code = [data[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letter in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_code)


generate_phonetic()
