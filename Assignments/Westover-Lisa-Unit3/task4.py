# Lisa Westover
# CS1400 7 week
# Unit3/Task4

# Elephants in the stall

import random
seeBothElephants = 0

# greeting
print("Welcome to the simulation of the zookeeper's elephant sightings.")
keepRunning = 1
# loop to re-run the simulation if wanted
while keepRunning == 1:
    print("Beginning simulation now...")
    for simulation in range(1, 1000000):
        elephant1 = random.randint(1, 6)
        elephant2 = random.randint(1, 6)
        zookeeper = random.randint(1, 6)

        if zookeeper == elephant1 and zookeeper == elephant2:
            seeBothElephants += 1

    totalSightings = format((100000 / seeBothElephants), "10.2f")
    print("The percentage of elephants seen by the zookeeper is: " + str(totalSightings))
    if float(totalSightings) >= 33:
        print("The zookeeper was right!")
    else:
        print("The custodian was right!")

    # returning to while loop to see if user wants to continue
    myAnswer = str(input("Keep running the simulation? (yes, no): "))
    if myAnswer == "yes":
        print("Here we go!")
    elif myAnswer == "no":
        keepRunning = 0
    else:
        print("Not a valid reply.  Thank you for playing!")
        keepRunning = 0


