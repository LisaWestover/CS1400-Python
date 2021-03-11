# Lisa Westover
# CS1400 7 week
# Unit2/Task1

#Investment Program

# Obtain starting investment, monthly payment, interest rate and years
investmentAmount = float(input("Enter the starting investment amount:"))
monthlyPaymentAmount = float(input("Enter the monthly payment amount:"))
annualInterestRate = float(input("Enter the annual interest rate as a percentage:"))
# Change interest rate percentage to decimal for FV formula
adjustedInterestRate = annualInterestRate * .01
# Break the annual interest rate into months
monthlyInterestRate = float(adjustedInterestRate / 12)
numberOfYears = eval(input("Enter the number of years for the loan:"))

# Calculate future value
futureValue = investmentAmount * ((1 + monthlyInterestRate) ** (numberOfYears * 12)) + monthlyPaymentAmount * (((1 + monthlyInterestRate) ** (numberOfYears * 12) - 1) / monthlyInterestRate) * (1 + monthlyInterestRate)

# output to screen
print("Future value:", format(futureValue, "6.2f"))