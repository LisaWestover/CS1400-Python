# Lisa Westover
# CS1400 7 week
# Unit3/Task1

# Random number guessing game

import random

print("Welcome to the Guessing Game\nThe Computer has picked a number from 1 - 10. Try to match it.")

# Generate random number
randomNumber = random.randint(1,10)

# Obtain user's guess, test that it is an integer
userGuess = input("What number do you choose (1 - 10):")
while not str.isdigit(userGuess):
    print("That is not a valid number.")
    userGuess = input("What number do you choose (1 - 10:")


# Genterate answer
if (int(userGuess) == randomNumber):
    msg = ("You picked " + str(userGuess) + ", and the actual number was " + str(randomNumber) + "." + "\nHonored to play with you, Master.")
elif (int(userGuess) == randomNumber - 1 or int(userGuess) == randomNumber + 1):
    msg = ("You picked " + str(userGuess) + ", and the actual number was " + str(randomNumber) + "." + "\nYou are a worthy opponent, Knight.")
elif (int(userGuess) == randomNumber - 2 or int(userGuess) == randomNumber + 2):
    msg = ("You picked " + str(userGuess) + ", and the actual number was " + str(randomNumber) + "." + "\nYou have much to lean, Padawan.")
elif (int(userGuess) == randomNumber - 3 or int(userGuess) == randomNumber + 3):
    msg = ("You picked " + str(userGuess) + ", and the actual number was " + str(randomNumber) + "." + "\nYoungling, your time will come.")
elif (int(userGuess) > randomNumber - 4 or int(userGuess) < randomNumber + 4):
    msg = ("You picked " + str(userGuess) + ", and the actual number was " + str(randomNumber) + "." + "\nKeep working hard in the Service Corps.")

# Output results to user
print(msg)