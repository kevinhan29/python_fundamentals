'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

a = (i for i in range(8))
print(a)

for i in a:
    print(i)