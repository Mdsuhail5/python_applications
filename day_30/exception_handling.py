import pandas

data = pandas.read_csv(r"day_30\nato_phonetic_alphabet (1).csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
finish = False
while not finish:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry,only letters in the alphabet please.")
    else:
        print(output_list)
        finish = True
