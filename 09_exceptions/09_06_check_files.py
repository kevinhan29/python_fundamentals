'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
sum_ = 0

try:
    with open(file_name, "r") as fin:
        contents = fin.readlines()
except FileNotFoundError as emsg1:
    print(emsg1)
except IOError as emsg2:
    print(emsg2)

for i in contents:
    try:
        temp = int(i)
    except ValueError:
        print("The first ")
    else:
        sum_ += temp

print(f"Sum of all values in {file_name} is {sum_}")