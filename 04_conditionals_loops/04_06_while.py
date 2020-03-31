'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

counter = 1             # used to count every 5th number
for i in range(1,101):
    if counter == 5:    # only print the number when the counter reaches 5
        print(i)
        counter = 1     # reset counter back to 1
        continue
    counter += 1        # increment counter
