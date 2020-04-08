'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

while True:
    try:
        num1 = float(input("Please enter in the number to be divided: "))
    except ValueError:
        print("That's not a number.")
    except Exception as e:
        print(e)
    else:
        break

while True:
    try:
        num2 = float(input("Please enter in the divisor number: "))
        if num2 == 0:
            raise Exception
    except ValueError:
        print("That's not a number")
    except Exception:
        print("Divisor cannot be 0")
    except:
        print("Something else went wrong")
    else:
        break

print(f"\n{num1/num2}\n")