# Lisa Westover
# CS1400 7 week
# Unit6/Task4

from modules.orbian import Orbian
from time import sleep
from random import randint # Hint hint
from random import shuffle # Hint hint


def main():
    print("WELCOME TO ORBIAN FAMILY")
    print()

    family = []
    input("Hit Enter to Create the First Four Orbians")

    for i in range(0, 4):
        name = input("\tEnter a name for Orbian " + str(i) + ": ")
        family.append(Orbian(name, 0, 0, randint(2, 6), randint(3, 9), randint(5, 16), 0))
        # Fill in with an anonymous object

    print("\tCreating your Orbian Family", end="")
    thinking()

    done = False

    while not done:
        print()
        print("Menu")
        print("\t1) Meet Orbian Family")
        print("\t2) Compare Orbians")
        print("\t3) Orbian Info")
        print("\t4) Create Orbian Baby")
        print("\t5) Send Orbian to Pasture")
        print("\t6) Orbian Thanos")
        print("\t7) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            meetTheOrians(family)
        elif choice == 2:
            compareOrians(family)
        elif choice == 3:
            orbianInfo(family)
        elif choice == 4:
            makeOrianBaby(family)
        elif choice == 5:
            sendOrianToPature(family)
        elif choice == 6:
            delOrianThanos(family) # This function call should return something
        elif choice == 7:
            done = True # Do not use break

    print("Thanks for playing Orbian Family!!!")

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def selectOrbian(family, selected=-1):
    for i in range(len(family)):
        print("\t" + str(i + 1) + " " + family[i].getName(), end="")
        if i == selected:
            print(" (already selected)")
        else:
            print()

    return int(input("Select an Orbian: ")) - 1

# Add all required functions below
def meetTheOrians(family):
    for i in family:
        print("I am Orbian " + str(i).capitalize())

def compareOrians(family):
    for i in range(0, len(family)):
        print(str([i + 1]) + " " + str(family[i]).capitalize())
    selectedOrbian1 = (eval(input("Select the first Orbian:")) - 1)
    for i in range(0, len(family)):
        print(str(i + 1) + ") " + str(family[i]), end=" ")
        if selectedOrbian1 == i:
            print(" (already selected)\n")
        else:
            print("")

    selectedOrbian2 = (eval(input("Select the second Orbian:")) - 1)
    print("Performing Analysis")
    thinking()
    if selectedOrbian1 == selectedOrbian2:
        comparison = "equal to"
    elif selectedOrbian1 > selectedOrbian2:
        comparison = "greater than"
    else:
        comparison = "less than"

    print("Orbian " + family[selectedOrbian1].getOName() + " is " + str(comparison) + " Orbian " + family[selectedOrbian2].getOName())

def orbianInfo(family):
    for i in range(0, len(family)):
        print(str([i + 1]) + " " + str(family[i]).capitalize())
    selectedOrbian = (eval(input("Select an Orbian to view:")) - 1)
    if family[selectedOrbian].getStatus() == "baby" and family[selectedOrbian].getOAge() >= 2:
        family[selectedOrbian].growToAdult()
        family[selectedOrbian].setStatus("adult")
    else:
        pass

    print("Orbian " + str(family[selectedOrbian]) + " is " + str(family[selectedOrbian].getOAge()) + " zungs old")
    print("and is " + str(family[selectedOrbian].setOVolume()) + " zogs, and " + str(len(family[selectedOrbian])) + " zings")

def makeOrianBaby(family):
    for i in range(0, len(family)):
        print(str([i + 1]) + " " + str(family[i]).capitalize())
    parent1 = (eval(input("Select the first Orbian parent:")) - 1)

    for i in range(0, len(family)):
        print(str(i + 1) + ") " + str(family[i]), end=" ")
        if parent1 == i:
            print(" (already selected)\n")
        else:
            print("")

    parent2 = (eval(input("Select the second Orbian parent:")) - 1)
    print("Creating Orbian Baby")
    thinking()
    babyOrbian = family[parent1] + family[parent2]
    family.append(babyOrbian)
    print("Greetings Orbian " + str(babyOrbian) + ", child of " + str(family[parent1]) + " and " + str(family[parent2]))


def sendOrianToPature(family):
    for i in range(0, len(family)):
        print(str([i + 1]) + " " + str(family[i]))
    delOrian = (eval(input("Select the Orbian to send to pasture:")) - 1)
    name = family[delOrian]
    family.pop(delOrian)
    print("Farewell dear " + str(name))
    thinking()


def delOrianThanos(family):
    print("Uh oh. Orbian Thanos just snapped his fingers", end=" ")
    thinking()
    halfOrians = len(family) // 2

    for i in str(halfOrians):
        shuffle(family)
        half = len(family) // 2
        #print(half)
        #family = family[0:half]
        for kill in range(0, half):
            family.pop()
        #family.pop(randint(0, len(family)))


main()