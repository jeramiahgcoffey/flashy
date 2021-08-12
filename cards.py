from tkinter import *
import pandas
import random


class Cards:
    def __init__(self):
        self.card_front = PhotoImage(file="images/card_front.png")
        self.card_back = PhotoImage(file="images/card_back.png")
        self.french_word = None
        self.english_word = None
        self.random_card = None
        # Create record from csv
        try:
            self.data = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            self.data = pandas.read_csv("data/french_words.csv")
        finally:
            self.word_dict_list = self.data.to_dict(orient="records")

    def new_card(self):
        # Select random card
        self.random_card = random.choice(self.word_dict_list)
        self.french_word = self.random_card["French"]
        self.english_word = self.random_card["English"]

    def remove_card(self):
        self.word_dict_list.remove(self.random_card)
        words_to_learn = pandas.DataFrame.from_dict(self.word_dict_list)
        with open("data/words_to_learn.csv", mode="w") as data:
            data.write(words_to_learn.to_csv(index=False))
