# Lisa Westover
# CS1400 7 week
# Unit7/Task1


from deck import Deck
from card import Card
import time

def main():
    players = []
    wagerBal = 100
    #obtain the number of players
    numPlayers = eval(input("How many players up to 5:"))
    for i in range(numPlayers):
        players.append(wagerBal)

    #obtain a bets list
    playerBet = []
    for i in range(numPlayers):
        playerBet.append(0)

    #create scorecard
    scoreCard = []
    for i in range(numPlayers):
        scoreCard.append([])
    #initialize the constructor
    deck = Deck()


    playAgain = True
    while playAgain:

        # create scorecard
        scoreCard = []
        for i in range(numPlayers):
            scoreCard.append([])

        dealerCard = []

        finalScore = []
        for i in range(numPlayers):
            finalScore.append(0)

        # create scorecard
        scoreCard = []
        for i in range(numPlayers):
            scoreCard.append([])

        print("NEW ROUND")
        #prompt the users to make their bet
        for i in range(len(players)):
            if players[i] == 0:
                continue
            else:
                print("Player" + str(i + 1) + " your balance is: " + str(players[i]))
                wager = eval(input("Player" + str(i + 1) + " place your bet, no less than $5:"))
                print("\n")
                if str(players[i]) > str(5) and str(wager) > str(4) and str(wager) < str(players[i]):
                    playerBet[i] = wager
                elif players[i] < 5:
                    playerBet[i] = players[i]
                else:
                    playerBet[i] = 5

        print(playerBet)
        dealHand(scoreCard, dealerCard, deck)
        addCards(scoreCard, dealerCard, finalScore, deck)
        dealerScore = calcDealer(dealerCard, deck)

        determineWinners(finalScore, dealerScore, playerBet, players)


        response = str(input("Do you want to play again? (y or n):"))
        if response == "y":
            playAgain = True
        elif response == "n":
            print("Thank you for playing!!")
            sortWinners(players)
            for i in range(len(players)):
                print("Player " + str(i + 1) + "'s final balance: " + str(players[i]))
            playAgain = False




def dealHand(scoreCard, dealerCard, deck):

    deck.shuffle()

    for j in range(2):
        print("\n")
        dealerCard.append(deck.draw())
        #print("Dealer" + "'s hand shows a " + str(dealerCard))
        print("Dealer is issued a card")
        for i in range(len(scoreCard)):
            scoreCard[i].append(deck.draw())
            #print("Player " + str(i + 1) + "'s hand shows a "+ str(scoreCard[i]))
            print("Player " + str(i + 1) + " is issued a card")
    print("The Dealer's second card is a " + str(dealerCard[1]))


def addCards(scoreCard, dealerCard, finalScore, deck):
    for i in range(len(scoreCard)):
        print("Player " + str(i + 1) + "'s hand shows a " + str(scoreCard[i]))
        keepDrawing = True
        while keepDrawing:
            hitMe = input("Would you like to take another card or hold? (h or k)")
            if hitMe == "h":
                scoreCard[i].append(deck.draw())
                print("Player " + str(i + 1) + "'s new card is a " + str(scoreCard[i]))
                playerTotal = calcTotal(scoreCard[i])
                if playerTotal > 21:
                    print("Bust!!")
                    finalScore[i] = playerTotal
                    keepDrawing = False
                else:
                    continue
            elif hitMe == "k":
                keepDrawing = False
                finalScore[i] = calcTotal(scoreCard[i])
            else:
                print("Invalid entry")


def calcDealer(dealerCard, deck):
    print("Dealer" + "'s hand shows a \n" + str(dealerCard))
    i = 0
    pointTotal = calcTotal(dealerCard)
    pointMax = 17
    while pointTotal < pointMax:
        print("The dealer selects another card")
        time.sleep(1)
        dealerCard.append(deck.draw())
        print("The dealer now has " + str(dealerCard))
        pointTotal = calcTotal(dealerCard)
        if pointTotal > 21:
            print("The dealer busts!")
            return pointTotal
        elif pointTotal > 16 and pointTotal <= 21:
            print("The dealer holds")
            return pointTotal
        else:
            return pointTotal
    return pointTotal

def calcTotal(scoreCard):
    maxValue = 0
    aceCount = 0
    for card in scoreCard:
        if card.getCardValue() == 1:
            aceCount += 1
            maxValue += 11
        elif card.getCardValue() > 10:
            maxValue += 10
        else:
            maxValue += card.getCardValue()

    while maxValue > 21 and aceCount > 0:
        aceCount -= 1
        maxValue -= 10

    return maxValue


def determineWinners(finalScore, dealerScore, playerBet, players):
    if dealerScore > 21:
        print("Dealer's " " score is " + str(dealerScore) + ": Loses")
    else:
        print("Dealer's score is " + str(dealerScore))

    for i in range(len(finalScore)):
        if finalScore[i] > 21:
            print("Player " + str(i + 1) + " score is " + str(finalScore[i]) + ": Loses")
            players[i] -= playerBet[i]
            print("\tBalance is: " + str(players[i]))
        elif int(dealerScore) > 21 and finalScore[i] < 22:
            print("Player " + str(i + 1) + " score is " + str(finalScore[i]) + ": Winner")
            players[i] += playerBet[i]
            print("\tBalance is: " + str(players[i]))
        elif dealerScore > finalScore[i]:
            print("Player " + str(i + 1) + " score is " + str(finalScore[i]) + ": Loses")
            players[i] -= playerBet[i]
            print("\tBalance is: " + str(players[i]))
        else:
            print("Player " + str(i + 1) + " score is " + str(finalScore[i]) + ": Winner")
            players[i] += playerBet[i]
            print("\tBalance is: " + str(players[i]))

def sortWinners(players):
    didSwap = True
    while didSwap:
        didSwap = False
        sortCnt = 1
        for i in range(len(players) - sortCnt):
            if players[i] > players[i + 1]:
                players[i], players[i + 1] = players[i + 1], players[i]
                didSwap = True
        sortCnt += 1


main()