# Lisa Westover
# CS1400 7 week
# Unit5/Task2

import math
import time

class Blobber:
    def __init__(self, color, name, vitalityBorn, calcVitality, vitality=1.0, radius=50.0, height=100.0):
        self.__color = str(color)
        self.__name = str(name)
        self.__radius = float(radius)
        #self.__radiusBorn = float(radiusBorn)
        self.__height = float(height)
        self.__vitalityBorn = float(vitalityBorn)
        self.__vitality = float(vitality)
        self.__calcVitality = float(calcVitality)
        self.__startTime = time.time()

    def getStartTime(self):
        return self.__startTime

    def getBlobberName(self):
        return self.__name

    def setBlobberName(self, name):
        self.__name = name
        return True

    def getBlobberColor(self):
        return self.__color

    def setBlobberColor(self, color):
        self.__color = color
        return True

    def getBlobberRadius(self):
        return self.__radius

    def setBlobberRadius(self, radius):
        self.__radius = radius
        return True

    #def getBlobberRadiusBorn(self, radiusBorn):
    #    return self.__radiusBorn


    #def setBlobberRadiusBorn(self, radiusBorn):
    #    self.__radiusBorn = radiusBorn
    #    return True

    def getBlobberHeight(self):
        return self.__height

    def setBlobberHeight(self, height):
        self.__height = height
        return True

    def getVitalityBorn(self):
        return self.__vitalityBorn

    def setVitalityBorn(self, radiusBorn, height):
        self.__vitalityBorn = float(math.pi * pow(radiusBorn, 2 * height))

    def setBlobberVitality(self):
        return self.__vitality

    def vitalsOK(self, currentSeconds):
        self.__vitality -= float(currentSeconds * 0.02)
        self.__calcVitality = self.__vitalityBorn / self.__vitality
        return True if self.__calcVitality >= .90 < 1.10 else False

    def feedBlobber(self, blobberFood, radius, height):
        self.__vitality += float(math.pi * pow(radius, 2 * height))
        return True

    def blobberSpeak(self):
        return "My name is ", self.getBlobberName, ". My vitality is at ", self.getBlobberVitality, "%"

    def __str__(self):
        return "My name is " + str(self.__name) + ". My vitality is at " + str(self.__vitality) + "%"

    def __repr__(self):
        return "Blobber vitality: " + format(str(self.__vitality), "8.4s")

    def getBlobberVitality(self):
        return self.__vitality




