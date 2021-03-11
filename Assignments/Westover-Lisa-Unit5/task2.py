# Lisa Westover
# CS1400 7 week
# Unit5/Task2


from blobber import Blobber

import time



def main():

    newColor = str()


    blobber = Blobber("","", 0,1.0)


    blobberName = str(input("Enter your Blobber's name:"))
    blobber.setBlobberName(blobberName)
    blobberColor = str(input("Enter your Blobber's color:"))
    blobber.setBlobberColor(blobberColor)
    blobberRadius = int(input("Enter your Blobber's radius:"))
    blobber.setBlobberRadius(blobberRadius)
    #blobber.setBlobberRadiusBorn(blobberRadius)
    blobberHeight = int(input("Enter your Blobber's height:"))
    blobber.setBlobberHeight(blobberHeight)
    #blobber.setVitalityBorn(radiusBorn, height)

    newName = str()
    done = False
    looped = 0

    while not done:
        currentSeconds = 0
        print("Main Menu")
        print("\t1) Display Name")
        print("\t2) Change Name")
        print("\t3) Display Color")
        print("\t4) Change Color")
        print("\t5) Feed Blobber")
        print("\t6) Blobber Speak")
        print("\t7) Quit")
        menuSelection = eval(input("Make a selection:"))


        if menuSelection == 1:
            print(blobber.getBlobberName())
        elif menuSelection == 2:
            blobber.setBlobberName(input("Enter the new name:"))
        elif menuSelection == 3:
            print(blobber.getBlobberColor())
        elif menuSelection == 4:
            blobber.setBlobberColor(input("Enter the new color:"))
        elif menuSelection == 5:
            blobber.feedBlobber(eval(input("How much food?:")), blobber.getBlobberRadius(), blobber.getBlobberHeight())
            currentSeconds = int(blobber.getStartTime()) % 60
            #print(currentSeconds)
            #print(blobber.getBlobberVitality)
            blobber.vitalsOK(currentSeconds)
        elif menuSelection == 6:
            blobber.blobberSpeak()
            currentSeconds = int(blobber.getStartTime()) % 60
            print(currentSeconds)
            blobber.vitalsOK(currentSeconds) if print(blobber) else print("DUST!!")
            print(blobber.getBlobberVitality)
        elif menuSelection == 7:
            done = True
        else:
            break



    print("Thanks for Playing")

main()