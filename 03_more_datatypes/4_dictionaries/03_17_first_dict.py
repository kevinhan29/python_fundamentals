'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

sqr_values = {1 : 1**2, 2 : 2**2, 3 : 3**3, 4 : 4**2}

print(sqr_values)
for i in range(len(sqr_values)):
    print(sqr_values[i+1])