'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

months = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", \
          "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}

user_input = input("Please enter a month in numerical format: ")

if months.get(user_input) == None:
    print("Other")
else:
    print(months[user_input])