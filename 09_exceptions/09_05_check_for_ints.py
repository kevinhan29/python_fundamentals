'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

while True:
    try:
        user_input = float(input("Please enter an integer: "))
        if not user_input.is_integer():     # if user input is not an int, then it's a float
            raise Exception
    except ValueError:
        print("That's not a number")
    except Exception:
        print("That's a float, not an integer")
    except:
        print('Something else went wrong')
    else:                                   # turn the input into an int
        user_input = int(user_input)
        break
    finally:
        print("")