# Lisa Westover
# CS1400 7 week
# Unit3/Task3


# Finding the Fluky Numbers

import random
import time
#obtain start time
startTime = time.time()

#myNum is a for loop that wraps this for loop and counts to 10,000
for myNum in range(1, 10000):
    sum = 0
    for possibleFactors in range(1, myNum):
        if myNum % possibleFactors == 0:
            #then it is a possibleFactor
            random.seed(possibleFactors)
            randNumber = random.randint(1, myNum)
            sum += randNumber
    if myNum == sum:
        print("Fluky Number: ", myNum)

#obtain endtime
endTime = time.time()
totalTime = format(endTime - startTime, ">5.0f")
print("Total Time: " + str(totalTime) + " seconds")
print("Total Loops: " + format(str(sum), ">7s"))

