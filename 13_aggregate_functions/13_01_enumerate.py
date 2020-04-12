'''
Demonstrate the use of the .enumerate() function.
'''

x = ['first', 'second', 'third']

for i, j in enumerate(x, start=1):
    print(i, j)