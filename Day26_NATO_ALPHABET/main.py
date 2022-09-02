import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
assigned_words = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word :").upper()

new_item = [assigned_words[letter] for letter in word]
print(new_item)
