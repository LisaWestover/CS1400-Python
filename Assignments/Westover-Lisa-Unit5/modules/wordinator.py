# Lisa Westover
# CS1400 7 week
# Unit5/Task3

class Wordinator:
    def __init__(self, sindgleWord):
        self.__word = sindgleWord

    def getWord(self):
        return self.__word

    def setWord(self):
        self.__word = singleWord
        return True

    def __lt__(self, other):
            i = 0
            while i < min(len(self.__word), len(other.getWord())):
                if self.__word[i] < other.getWord()[i]:
                    return self.__word
                elif self.__word[i] == other.getWord()[i]:
                    i += 1
                else:
                    return other.getWord()


    def __str__(self):
        return str(self.__word)
    def __repr__(self):
        return "Wordinator: "



    def __add__(self, other):
        return self.__word.capitalize() + other.getWord().capitalize()

    def __mul__(self, other):
        output = ""
        i = 0
        while i < other:
            output += self.__word
            i += 1
        return output.upper()

    def __truediv__(self, other):
        self.__word = self.__word.capitalize()
        minLength1 = len(self.__word)
        minLength2 = len(other.getWord())
        minWord = ""
        if len(self.__word) < len(other.getWord()):
            minWord = self.__word.capitalize()
            maxWord = other.getWord().capitalize()
        else:
            minWord = other.getWord()
            maxWord = self.__word

        output = ""

        i = 0
        while i < len(minWord):
            output += self.__word[i]
            output += other.getWord()[i]
            i += 1
        while minLength1 < minLength2:
            output += maxWord[minLength1]
            minLength1 += 1
        return output

    def __mod__(self, other):
        output = ""
        length1, length2 = len(self.__word), len(other.getWord())

        i = 0
        while i < length1:
            if len(self.__word) % 2 == 0:
                calcStartInnerWord = round(length1 * .25)
                calcEndInnerWord = round(length1 * .75)
            else:
                calcStartInnerWord = round((length1 - 1) * .25)
                calcEndInnerWord = round(length1 + 1 * .75)
            output += self.__word[calcStartInnerWord]
            if length1 > calcEndInnerWord:
                break
            else:
                i += 1

        j = 0
        while j < length1:
            if len(other.getWord()) % 2 == 0:
                calcStartInnerWord = round(length2 * .25)
                calcEndInnerWord = round(length2 * .75)
            else:
                calcStartInnerWord = round((length2 - 1) * .25)
                calcEndInnerWord = round(length2 + 1 * .75)
            output += self.__word[calcStartInnerWord]
            if length2 > calcEndInnerWord:
                break
            else:
                j += 1
        return output


    def __sub__(self, other):
        word1 = other.getWord()
        word2 = self.__word
        return word1, word2

    def __len__(self, other):
        word1 = word1.slice(-1)
        word2 = word2.slice(-1)
        return word1, word2


'''
    
    def __truediv__(self, other):
        #self word and other and mix accourding to descrition
        return self.__word / other.getWord()

    def mixWords(self, wordinator1, other):
        i = 0
        setMin = min(len(self.__word), len(other.getWord()))
        setMax = max(len(self.__word), len(other.getWord()))
        newWord = ""
        while i < setMin:
            newWord += self.__word[i] + other.getWord()[i]
            i += 1
        if setMax == len(self.__word):
            while setMin < setMax:
                newWord += self.__word[setMin]
        else:
            while setMin < setMax:
                newWord += other.getWord()[setMin]




'''










'''

    

    def midWords(self,wordinator1, wordinator2):

    def switchCaseWords(self,wordinator1, wordinator2):

    def backWordsSlice(self,wordinator1, wordinator2):

    def backWordsManual(self,wordinator1, wordinator2):
'''




