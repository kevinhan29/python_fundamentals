'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

# ask user for an integer
while True:
    try:                # check whether input is an integer or not
        x = int(input("\nEnter an integer between 0 and 1,000,000,000: "))
        #print(is_int)
    except:
        print("\nThat's not an integer!")
        continue
    if 0 <= x <= 1000000000:
        break
    else:
        print("\nThat number is out of range!")

found = False           # keeps track if the number is found
count = 0               # counts numbers up to 1 million

''' below block of code took way too long for numbers close to 1 billion, will use different method
# use while loop to count up by 1 from 0 until the number is found
while not found:
    print(count)
    if count == x:
        print("\nFound it! Your number is", count)
        found = True
    else:
        count += 1
        print("+")
'''

floor = 0
ceiling = 1000000000
guess = (ceiling - floor)//2

while not found:
    print(guess)
    if guess == x:
        print("\nFound it! Your number is", guess)
        found = True
    elif guess > x:         # If guess is larger than user input, make a new guess that's halfway between the floor and current guess
        ceiling = guess
        guess = (ceiling - floor)//2
        print("greater than")
    else:                   # if guess is lower than user input, make a new guess that's halfway between current guess and ceiling
        floor = guess
        guess = (ceiling - floor)//2 + guess
        print("lower than")
