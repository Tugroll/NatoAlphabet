import pandas



nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")


nato_alp_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

print(nato_alp_dict)


input_word = input("Enter a word \n").upper()

letters_word = [nato_alp_dict[letter] for letter in input_word]

print(letters_word)
