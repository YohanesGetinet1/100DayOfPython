#!/usr/bin/python3

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
assigned_words = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word :").upper()
    try:
        new_item = [assigned_words[letter] for letter in word]
    except KeyError:
        print("Sorry, Insert letters from the alphabet only!")
        generate_phonetic()
    else:
        print(new_item)


generate_phonetic()
