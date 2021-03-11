# Lisa Westover
# CS1400 7 week
# Unit7/Task2

from random import randint
count = 0
# Remember how to use this kind of variable?


def main():

    print("Welcome to Recursion Fun")

    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4)))

    print()

    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):
        if randint(0, 2) == 0:
            numList.append(i)

    numPos = binarySearch(numList, key)

    if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))

    print("Total recursive calls: " + str(count))

def aggienacci(value):
    x = value
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return (aggienacci(x - 3) + aggienacci(x - 2)) / aggienacci(x - 1)

def binarySearch(numList, key):
    list = numList
    low = 0
    high = len(numList) -1
    return binarySearchRecursive(list, key, low, high)

def binarySearchRecursive(list, key, low, high):
    global count
    count += 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if key == list[mid]:
        return mid
    elif key < list[mid]:
        return binarySearchRecursive(list, key, low, mid -1)
    else:
        return binarySearchRecursive(list, key, mid + 1, high)


main()

