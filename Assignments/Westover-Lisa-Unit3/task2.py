# Lisa Westover
# CS1400 7 week
# Unit3/Task2

#Social Situation Analysis

import math

#query information from user1 and user2

print("Welcome to the Social Situation Analyzer System")
print("Person One")
user1Name = input("\tEnter your name:")
user1x, user1y = eval(input("\tEnter your position (x, y):"))
user1Radius = eval(input("\tEnter your personal space radius:"))
print("\nPerson Two")
user2Name = input("\tEnter your name:")
user2x, user2y = eval(input("\tEnter your position (x, y):"))
user2Radius = eval(input("\tEnter your personal space radius:"))


#calc distance between 2 people
distance = math.sqrt((user1x - user1y) ** 2 + ((user2x-user2y)**2))

#calc if personal space violated

user1SpaceViolated = -1
user2SpaceViolated = -1

if user1Radius + user2Radius < distance:
    user1SpaceViolated = 0
    user2SpaceViolated = 0
elif user1Radius > distance and user2Radius > distance:
    user1SpaceViolated = 1
    user2SpaceViolated = 1
elif user1Radius > distance:
    user1SpaceViolated = 1
    user2SpaceViolated = 0
elif user2Radius > distance:
    user1SpaceViolated = 0
    user2SpaceViolated = 1
else:
    print("Error with Radius and Personal Space")

#calc overlapping of radius'
usersOverlap = -1
if distance - (user1Radius + user2Radius) > 0:
    usersOverlap = 0
else:
    usersOverlap = 1

#calc if user is entirely in other user's space
user1inSpace = 0
user2inSpace = 0
if distance + user1Radius < user2Radius:
    user1inSpace = 1
elif distance + user2Radius < user1Radius:
    user2inSpace = 1
elif distance == 0 and user1Radius == user2Radius:
    user1inSpace = 1
    user2inSpace = 1

#calc personal space messages
if user1SpaceViolated and user2SpaceViolated:
    msgPersonTest = str(user1Name) + " and " + str(user2Name) + " are in each other's personal space"
elif user1SpaceViolated:
    msgPersonTest = str(user2Name) + " is in " + str(user1Name) + "'s personal space"
elif user2SpaceViolated:
    msgPersonTest = str(user1Name) + " is in " + str(user2Name) + "'s personal space"
else:
    msgPersonTest = "Neither " + str(user1Name) + " nor " + str(user2Name) + " is in the other's personal space"

#calc overlap messages
if not usersOverlap:
    msgOverlap = str(user1Name) +  " and " + str(user2Name) + "'s personal spaces do not overlap"
elif user1inSpace and user2inSpace:
    msgOverlap = str(user1Name) +  " and " + str(user2Name) + "'s personal spaces overlap"
elif user1inSpace:
    msgOverlap = str(user1Name) + "'s personal space is entirely inside " + str(user2Name) + "'s personal space"
elif user2inSpace:
    msgOverlap = str(user2Name) + "'s personal space is entirely inside " + str(user1Name) + "'s personal space"
else:
    msgOverlap = "Error"

#print final message

print("\nSocial Situation Analysis Results")
print("\t", msgPersonTest)
print( "\t", msgOverlap)