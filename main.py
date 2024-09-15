import pandas



nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")


nato_alp_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

print(nato_alp_dict)





def translate_func():
    input_word = input("Enter a word \n").upper()
    try:
        letters_word = [nato_alp_dict[letter] for letter in input_word]
    except KeyError:
        print("only letter please")
        translate_func()
    else:
        print(letters_word)

translate_func()
