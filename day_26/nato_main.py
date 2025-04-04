import pandas as pd

data = pd.read_csv(r"day_26\nato_phonetic_alphabet.csv")
df = pd.DataFrame(data)

# for (index, row) in df.iterrows():
#     print(index)
#     print("-"*8)
#     print(row)


new_df = {row.letter: row.code for (index, row) in df.iterrows()}
# print(new_df)

user_input = input("Enter your name: ").upper()

phonetic = [new_df[item] for item in user_input]
print(phonetic)
