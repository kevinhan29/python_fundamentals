'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

# take in Fahrenheit reading from console
F = float(input("Please enter a temperature in Fahrenheit: "))
C = (F - 32)*(5/9)      # convert to Celsius

# output conversion results
print(F, " degrees fahrenheit = ", C, " degrees celsius")