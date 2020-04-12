'''
Write a script with a function that demonstrates the use of *args.

'''
''

def adder(*args):
    sum_ = args[0]
    for i in range(1, len(args)):
        sum_ = sum_ + args[i]
    return sum_

print(adder(2,4,5,9,3))

print(adder("Hello", " ", "World"))