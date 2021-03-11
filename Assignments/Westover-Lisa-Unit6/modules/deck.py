from modules.gronkyutil import TITLE, GANG
from modules.card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        totalCards = 102 # Do not use a numeric literal

        for i in range(totalCards):
            self.__deck.append(Card(i))
            #<Fill-In> # Single line of code

        shuffle(self.__deck)

    def draw(self):
        return self.__deck.pop()
        #<Fill-In - returns a card> # Single line of code

