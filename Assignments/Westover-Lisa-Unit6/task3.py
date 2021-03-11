# Lisa Westover
# CS1400 7 week
# Unit6/Task3

from modules.deck import Deck
from time import sleep
from modules.gronkyutil import convertCardToId
from modules.gronkyutil import TITLE, GANG

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    playerHand = []
    cardTitle = ""
    cardGang = ""

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        playerHand.append(deck.draw())

    done = False
    while not done:
        print()
        print("Menu")
        print("\t(1) Display hand")
        print("\t(2) Sort by title")
        print("\t(3) Sort by gang")
        print("\t(4) Search for card")
        print("\t(5) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            displayHand(playerHand)
        elif choice == 2:
            sortByTitle(playerHand)
            #<Fill-In - Sort by Title> # Single line
        elif choice == 3:
            sortByGang(playerHand)
            #<Fill-In - Sort by gang> # Single line
        elif choice == 4:
            searchForACard(cardTitle, cardGang, playerHand)
            #<Fill-In - search for card> # Single line
        elif choice == 5:
            print("Thanks for playing!!")
            done = True
            #<Fill-In - quit leave a message> # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(playerHand):
    print("Your cards:")
    for i in playerHand:
       print(str(i))
    # print(playerHand)

def sortByTitle(playerHand):
    print("Bubble Sort by Title", end=" ")
    thinking()
    didSwap = True
    while didSwap:
        didSwap = False
        sortCnt = 1
        for i in range(len(playerHand) - sortCnt):
            if TITLE.index(playerHand[i].getTitle()) > TITLE.index(playerHand[i + 1].getTitle()):
                playerHand[i], playerHand[i + 1] = playerHand[i + 1], playerHand[i]
                didSwap = True
        sortCnt += 1

def sortByGang(playerHand):
    print("Selection Sort by Gang", end=" ")
    fillIndex = 0
    currMinIndex = 0
    for i in range(len(playerHand) - 1):
        currMinIndex = i
        for j in range(i + 1, len(playerHand)):
            if GANG.index(playerHand[currMinIndex].getGang()) > GANG.index(playerHand[j].getGang()):
                currMinIndex = j
        if currMinIndex != fillIndex:
            playerHand[i], playerHand[currMinIndex] = playerHand[currMinIndex], playerHand[i]

def searchForACard(cardTitle, cardGang, playerHand):
    print("Search for a card")
    for i in range(1, len(TITLE) + 1):
        print("\t(" + str(i) + ") ", TITLE[i - 1])

    cardTitle = eval(input("Choose a Title: "))
    newCardTitle = TITLE[cardTitle - 1]

    #need a manu displaying all the gangs

    for i in range(1, len(GANG) + 1):
        print("\t(" + str(i) + ") ", GANG[i - 1])
    cardGang = eval(input("Choose a Gang: "))
    newCardGang = GANG[cardGang -1]
    key1 = TITLE[cardTitle - 1] + " of " + GANG[cardGang - 1]
    key = convertCardToId(newCardTitle, newCardGang)


    print("Insertion Sort by Title", end=" ")
    thinking()
    for i in range(i, len(playerHand)):
        currElement = playerHand[i]
        j = i - 1

        while j >= 0 and playerHand[j].getID() > currElement.getID():
            playerHand[j + 1] = playerHand[j]
            j -= 1
        playerHand[j + 1] = currElement


    print("Binary Search", end=" ")
    thinking()
    high = len(playerHand)
    low = 0

    success = False
    while high >= low:
        mid = (high + low) // 2
        if key == playerHand[mid].getID():
            success = True
            break
        elif key < playerHand[mid].getID():
            high = mid - 1
        else:
            low = mid + 1


    if success == True:
        print("Congrats! You have that card")
    else:
        print("Sorry. You do not have that card")



main()