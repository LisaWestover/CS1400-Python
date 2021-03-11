# Lisa Westover
# CS1400 7 week
# Unit6/Task4

from random import randint, shuffle
import time
from math import pi


class Orbian:
    def __init__(self, oName, oAge, oVolume, oHeadRadius, oBodyRadius, oBodyHeight, oTotalHeight):
        self.__oName = oName
        self.__oAge = oAge
        self.__oVolume = oVolume
        self.__oHeadRadius = oHeadRadius
        self.__oBodyRadius = oBodyRadius
        self.__oBodyHeight = oBodyHeight
        self.__totalHeight = oTotalHeight
        self.__startTime = time.time()
        self.__status = "baby"



    def getOName(self):
        return self.__oName

    def setOName(self, oName):
        self.__oName = oName

    def getOAge(self):
        endTime = time.time()
        totalTime = endTime - self.__startTime
        #print("Total Time: " + str(totalTime) + " seconds")
        self.__oAge = round(totalTime / 5, 2)
        return self.__oAge

    def setOAge(self, oAge):
        self.__oAge = oAge

    def getOVolume(self):
        return self.__oVolume

    def setOVolume(self):
        headVolume = float((4 / 3) * pi * self.__oHeadRadius)
        bodyVolume = float(pi * pow(self.__oBodyRadius, 2) * self.__oBodyHeight)
        self.__oVolume = round(headVolume + bodyVolume, 2)
        return self.__oVolume

    def __len__(self):
        return self.__oBodyHeight

    def getOHeadRadius(self):
        return self.__oHeadRadius

    def setOHeadRadius(self):
        self.__oHeadRadius = oHeadRadius

    #def getOBodyRadius(self):
        #return self.__oBodyRadius = oBodyRadius
    #    pass

    def setOBodyRadius(self):
        self.__oBodyRadius = oBodyRadius

    #def getOBodyHeight(self):
    #    #return self.__oBodyHeight = oBodyHeight
    #    pass

    #def setOBodyHeight(self):
    #    self.__oBodyHeight = oBodyHeight

    #def setOTotalHeight(self):
    #    pass

    def __add__(self, other):
        partialName1 = list(self.__oName)
        shuffle(partialName1)
        partialName2 = list(other.getOName())
        shuffle(partialName2)
        partialName1 = "".join(partialName1)
        partialName2 = "".join(partialName2)
        partialName1 = partialName1[0: len(self.__oName) // 2]
        partialName2 = partialName2[0: len(other.getOName()) // 2]
        newName = partialName1 + partialName2
        babyOrbian = Orbian(newName, 0, 0, randint(2, 6), randint(3, 9), randint(5, 16), 0)
        return babyOrbian

    def growToAdult(self):
        self.__oHeadRadius = self.__oHeadRadius * 2
        self.__oBodyRadius = self.__oBodyRadius * 2
        self.__oBodyHeight = self.__oBodyHeight * 3

    def __repr__(self):
        return "\t" + self.getOName()

    def __str__(self):
        return self.getOName()

    def __eq__(self, other):
        if self.getOVolume() == other.getOVolume():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.getOVolume() > other.getOVolume():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.getOVolume() < other.getOVolume():
            return True
        else:
            return False

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

