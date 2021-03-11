# Lisa Westover
# CS1400 7 week
# Unit6/Task2


def main():
    myArray = []
    i = True
    while i == True:
        num = input("Enter a number:")
        if num.isdigit():
            myArray.append(eval(num))
        else:
            i = False


    print("Number of values entered: ", len(myArray))
    print("Maximum value: ", max(myArray))
    print("Minimum value: ", min(myArray))
    print("Sum of all values: ", sum(myArray))
    print("Average value: ", format(sum(myArray) / len(myArray), "8.2f"))


main()
