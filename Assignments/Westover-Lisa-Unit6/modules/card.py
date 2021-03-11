from modules.gronkyutil import TITLE, GANG

class Card:
    def __init__(self, id):
        self.__id = id

    def getTitle(self):
        return TITLE[self.__id // 17] # Do not use a numeric literal

    def getGang(self):
        return GANG[self.__id % 6] # Do not use a numeric literal

    def getID(self):
        return self.__id

    # Add two dunder methods below to meet assignment requirements
    def __repr__(self):
        return "\t" + self.getTitle() + " of " + self.getGang()

    def __str__(self):
        return self.__repr__()

    # def __gt__(self, playerHand, i):
    #      return True if self.getTitle[i] > self.getTitle[i + 1]
