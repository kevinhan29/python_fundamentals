'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

# prompts user for values
P = int(input("Please enter the amount of money you'd like to invest: "))
R = float(input("Please enter the interest rate: "))
R = R/100
T = int(input("Please enter the number of years you'd like to invest: "))

# calculate future value and prints it out
exp = 12*T
FV = P*((1+(R/12))**exp)
print("Your future value is $", FV)