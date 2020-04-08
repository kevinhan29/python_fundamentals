'''
Write a script that demonstrates a try/except/else.

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