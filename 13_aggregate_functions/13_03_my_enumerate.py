'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(my_list, start=0):
    return ((i + start, my_list[i]) for i in range(len(my_list)))

x = ["zero", "one", "two", "three"]
y = my_enumerate(x, 1)

print(y)
for i, j in y:
    print(i, j)
