'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

x = [5, 1111, 9, 0, 8888, 983, 50938239, 192838, 9301, 9999]

gen = (i for i in x if i%1111 == 0)

for i in gen:
    print(i)