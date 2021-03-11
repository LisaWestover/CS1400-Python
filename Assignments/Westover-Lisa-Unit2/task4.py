# Lisa Westover
# CS1400 7 week
# Unit2/Task4

#Net Pay program

import math

employeesName = ""
numberOfHoursWorked = 0
hourlyRateOfPay = 0.0
federalTaxWithholdingRate = 0.0
stateTaxWithholdingRate = 0.0

#obtain input from user
employeesName = input("Enter employee's name:").upper()
numberOfHoursWorked = input("Enter the number of hours worked in a week:")
hourlyRateOfPay = input("Enter hourly pay rate:")
federalTaxWithholdingRate = input("Enter federal tax withholding rate (ex. 0.12):")
stateTaxWithholdingRate = input("Enter state tax withholding rate (ex. 0.06):")
print("\n\n")
#calculate Gross Pay, Fed Withhodings, State Withholdings, Total Deductions, and Net Pay
gross_Pay = 0.0
fedWithholdings = 0.0
stateWithholdings = 0.0
totalDeductions = 0.0
netPay = 0.0

gross_Pay = float(numberOfHoursWorked) * float(hourlyRateOfPay)
fedWithholdings = gross_Pay * float(federalTaxWithholdingRate)
stateWithholdings = gross_Pay * float(stateTaxWithholdingRate)
totalDeductions = fedWithholdings + stateWithholdings
netPay = float(gross_Pay) - totalDeductions
gross_Pay = format(gross_Pay, "10.2f")
fedWithholdings = format(fedWithholdings, "10.2f")
stateWithholdings = format(stateWithholdings, "10.2f")
totalDeductions = format(totalDeductions, "10.2f")
netPay = format(netPay, "10.2f")

#output information with proper formatting

titleHeader = format(employeesName + " PAY INFORMATION", ">35s")
titleSubHeader1 = format("Pay", ">30s")
msgNumberOfHoursWorked = format("Hours Worked:", ">35s") + format(numberOfHoursWorked, ">21s")
msgPayRate = format("Pay Rate: $    ", ">41s") + format(hourlyRateOfPay, ">15s")
msgGrossPay = format("Gross Pay: $    ", ">41s") + format(gross_Pay, ">15s")
titleSubHeader2 = format("Deductions", ">34s")
msgFederalWithholdings = format("Federal Withholding (" +str(federalTaxWithholdingRate) + "): $    ", ">41s") + format(str(fedWithholdings), ">15s")
msgStateWithholdings = format("State Withholding (" + str(stateTaxWithholdingRate) + "): $    ", ">41s") + format(str(stateWithholdings), ">15s")
msgTotalDeductions = format("Total Deductions: $    ", ">41s") + format(totalDeductions, ">15s")
msgNetPay = format("Net Pay: $    ", ">41s") + format(netPay, ">15s")


msgMaster = (titleHeader + "\n" + titleSubHeader1 + "\n" + msgNumberOfHoursWorked + "\n" + msgPayRate + "\n" + msgGrossPay + "\n\n" + titleSubHeader2 + "\n" + msgFederalWithholdings + "\n" + msgStateWithholdings + "\n" + msgTotalDeductions + "\n\n" + msgNetPay)
print(msgMaster)