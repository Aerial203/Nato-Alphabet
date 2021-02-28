import pandas

nato_phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")

data = {value.letter: value.code for (index, value) in nato_phonetic_data.iterrows()}


user_input = input("Enter a word: ").upper()

phonetic_code = [data[letter] for letter in user_input]
print(phonetic_code)
