'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

# prompt user to enter 10 integers and store into a list
num_list = []
for x in range(10):
    temp = int(input("Please enter an integer: "))
    num_list.append(temp)
#print(num_list)

even_list = []         # list to hold 2nd, 4th, etc entered objects
odd_list = []          # list to hold 1st, 3rd, etc entered objects
odd = True             # variable for keeping track of odd or even entered object

# store alternating objects into odd and even lists
for x in range(len(num_list)):
    if odd:
        odd_list.append(num_list.pop(0))
        odd = False
        #print(odd_list)
    else:
        even_list.append(num_list.pop(0))
        odd = True
        #print(even_list)

# combine list with even objects ascending and odd objects descending
odd_list.reverse()
sorted_list = even_list + odd_list

# print out results
print(*sorted_list, sep=", ")
