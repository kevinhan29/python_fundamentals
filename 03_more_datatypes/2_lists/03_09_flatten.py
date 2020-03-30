'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

flattened = []          # initialize flattened list

# read through each object in the master list
for i in starting_list:
    for j in i:
        flattened.append(j)

print(flattened)
